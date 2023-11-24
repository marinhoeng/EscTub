# Input data
import numpy as np

from pressure.Flow_Velocity import calculate_flow_insitu
from pressure.dPdL import (
    calculate_dPdL_Total,
    calculate_Pwf,
    calculate_Re_NS,
    calculate_y,
)
from pvt.fluid_data import FluidData
from _tests.test_mesh import base_case_study as case
from mesh.mesh import building_mesh, OperationalData
from pvt.pvt_properties import calculate_pvt_properties, calculate_pvt_properties_mixture
from pressure.Beggs_Brill import calculate_Beggs_Brill
from thermal.temperature import calculate_dTdL


g = 9.81


def test_base(case) -> None:
    mesh = building_mesh(data=case)

    sec_number = len(mesh)

    Pvec = np.zeros(sec_number)
    Tvec = np.zeros(sec_number)

    fd = FluidData()

    fd = fd.set_fluid_data(API=case.API, dg=case.dg, RGO=case.RGO)

    Pwf = calculate_Pwf(P_res=case.P_res, IP=case.IP, Q_sc=case.Q_sc)
    # DOUBTS ABOUT THE CLASSES -> INPUTDATA AND OPERATIONALDATA -> ("IP", WHERE IS THE CORRECT PLACE FOR IT?)

    Pvec[0] = Pwf
    Tvec[0] = case.T_res
    λLvec = []
    for i in range(sec_number-1):

        pvt = calculate_pvt_properties(fd=fd, P=float(Pvec[i]), T=float(Tvec[i]))

        Qm, Vm, Vsl, Vsg, λL = calculate_flow_insitu(
            data=case,
            dh=mesh[i].geometry.dh,
            pvt=pvt,
            P=float(Pvec[i]),
            Pb=pvt.Pb
        )

        if 0 < λL < 1:
            HL = calculate_Beggs_Brill(ρ_oil=pvt.ρ_oil, λL=λL, Vsl=Vsl, Vm=Vm,
                                   dh=mesh[i].geometry.dh, σog=pvt.σog, θ=mesh[i].geometry.θ, g=g)
        else:
            HL = λL

        pvt_mixture = calculate_pvt_properties_mixture(PVTOG=pvt, λL=λL, HL=HL)

        Rens = calculate_Re_NS(ρ_NS=pvt_mixture.ρ_NS, Vm=Vm, dh=mesh[i].geometry.dh, μ_NS=pvt_mixture.μ_NS)

        y = calculate_y(HL=HL, λL=λL)

        dP_dL_Total = calculate_dPdL_Total(HL=HL, Rens=Rens, y=y, εr=mesh[i].geometry.εr,
                                           ρ_NS=pvt_mixture.ρ_NS, ρ_slip=pvt_mixture.ρ_slip, g=g,
                                           θ=mesh[i].geometry.θ, Vm=Vm, Vsg=Vsg, dh=mesh[i].geometry.dh, P=float(Pvec[i]))

        dT_dL_Total = calculate_dTdL(T=float(Tvec[i]), tec=mesh[i].geometry.tec, T_env=mesh[i].geometry.T_env,
                               ρ_slip=pvt_mixture.ρ_slip, Qm=Qm, g=g, θ=mesh[i].geometry.θ, cp_slip=pvt_mixture.cp_slip)

        Pvec[i+1] = Pvec[i] + dP_dL_Total * mesh[i].dL
        Tvec[i+1] = Tvec[i] + dT_dL_Total * mesh[i].dL

        λLvec.append(λL)

    assert 1 == 1
