# Input data
import numpy as np

from pressure.Flow_Velocity import calculate_flow_insitu
from pressure.dPdL import *
from pvt.fluid_data import FluidData
from pvt.pvt_properties import PVTProperties
from _tests.test_mesh import base_case_study as case
from mesh.mesh import building_mesh, OperationalData
from pvt.pvt_properties import calculate_pvt_properties
from pressure.Beggs_Brill import calculate_Beggs_Brill
from thermal.temperature import calculate_dTdL


g = 9.81


def test_flow_analysis(case) -> None:
    mesh = building_mesh(data=case)

    sec_number = len(mesh)

    Pvec = np.zeros(sec_number)
    Tvec = np.zeros(sec_number)

    fd = FluidData()

    fd = fd.set_fluid_data(API=case.API, dg=case.dg, RGO=case.RGO)

    op = OperationalData()

    Pwf = calculate_Pwf(P_res=op.P_res, IP=op.IP, Q_sc=op.Q_sc)
    # DOUBTS ABOUT THE CLASSES -> INPUTDATA AND OPERATIONALDATA -> ("IP", WHERE IS THE CORRECT PLACE FOR IT?)

    for i in range(sec_number):
        Tvec[i] = case.T_res
        Pvec[i] = case.P_res

        pvt = calculate_pvt_properties(fd=fd, P=float(Pvec[i]), T=float(Tvec[i]))

        Qm, Vm, Vsl, Vsg, λL = calculate_flow_insitu(
            data=case,
            dh=mesh[i].geometry.dh,
            pvt=pvt,
            P=float(Pvec[i]),
            Pb=pvt.Pb
        )

        HL = calculate_Beggs_Brill(ρ_oil=pvt.ρ_oil, λL=λL, Vsl=Vsl, Vm=Vm,
                                   dh=mesh[i].geometry.dh, σog=pvt.σog, θ=mesh[i].geometry.θ, g=g)

        pvt_mixture = calculate_pvt_properties(fd=fd, P=float(Pvec[i]), T=float(Tvec[i]), λL=λL, HL=HL)

        Rens = calculate_Re_NS(ρ_NS=pvt_mixture.ρ_NS, Vm=Vm, dh=mesh[i].geometry.dh, μ_NS=pvt_mixture.μ_NS)

        y = calculate_y(HL=HL, λL=λL)

        dP_dL_Total = calculate_dPdL_Total(HL=HL, Rens=Rens, y=y, εr=mesh[i].geometry.εr,
                                           ρ_NS=pvt_mixture.ρ_NS, ρ_slip=pvt_mixture.ρ_slip, g=g,
                                           θ=mesh[i].geometry.θ, Vm=Vm, Vsg=Vsg, dh=mesh[i].geometry.dh, Pwf=Pwf)

        dT_dL = calculate_dTdL(T=float(Tvec[i]), tec=mesh[i].geometry.tec, T_env=mesh[i].geometry.T_env,
                               ρ_slip=pvt_mixture.ρ_slip, Qm=Qm, g=g, θ=mesh[i].geometry.θ, cp_slip=pvt_mixture.cp_slip)

    assert dP_dL_Total == 1

    assert dT_dL == 1
