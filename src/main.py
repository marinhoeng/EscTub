# Input data
import numpy as np
from numpy.typing import NDArray
from attrs import define
from pressure.Flow_Velocity import calculate_flow_insitu
from pressure.dPdL import (
    calculate_dPdL_Total,
    calculate_Pwf,
    calculate_Re_NS,
    calculate_y,
)
from pvt.fluid_data import FluidData
from mesh.mesh import building_mesh, InputData
from pvt.pvt_properties import (calculate_pvt_properties,
                                calculate_pvt_properties_mixture,
                                )
from pressure.Beggs_Brill import calculate_Beggs_Brill
from thermal.temperature import calculate_dTdL

g = 9.81


@define(frozen=True)
class ResultsData:
    Pvec: NDArray[np.float64]
    Tvec: NDArray[np.float64]
    MD: NDArray[np.float64]
    HLvec: NDArray[np.float64]
    ρ_slip_vec: NDArray[np.float64]
    μ_slip_vec: NDArray[np.float64]
    Pb_vec: NDArray[np.float64]
    Rs_vec: NDArray[np.float64]
    Bo_vec: NDArray[np.float64]
    ρ_oil_vec: NDArray[np.float64]
    ρ_gas_vec: NDArray[np.float64]
    μ_oil_vec: NDArray[np.float64]
    μ_gas_vec: NDArray[np.float64]


def run_analysis(case: InputData) -> ResultsData:
    mesh = building_mesh(data=case)

    sec_number = len(mesh)

    Pvec = np.zeros(sec_number)
    Tvec = np.zeros(sec_number)
    MD = np.zeros(sec_number)
    λLvec = np.zeros(sec_number)
    HLvec = np.zeros(sec_number)
    ρ_slip_vec = np.zeros(sec_number)
    μ_slip_vec = np.zeros(sec_number)
    Pb_vec = np.zeros(sec_number)
    Rs_vec = np.zeros(sec_number)
    Bo_vec = np.zeros(sec_number)
    ρ_oil_vec = np.zeros(sec_number)
    ρ_gas_vec = np.zeros(sec_number)
    μ_oil_vec = np.zeros(sec_number)
    μ_gas_vec = np.zeros(sec_number)

    fd = FluidData()

    fd = fd.set_fluid_data(API=case.API, dg=case.dg, RGO=case.RGO)

    Pwf = calculate_Pwf(P_res=case.P_res, IP=case.IP, Q_sc=case.Q_sc)
    # DOUBTS ABOUT THE CLASSES -> INPUTDATA AND OPERATIONALDATA -> ("IP", WHERE IS THE CORRECT PLACE FOR IT?)

    Pvec[0] = Pwf
    Tvec[0] = case.T_res
    MD[0] = mesh[0].MDf

    for i in range(sec_number - 1):

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
                                           θ=mesh[i].geometry.θ, Vm=Vm, Vsg=Vsg, dh=mesh[i].geometry.dh,
                                           P=float(Pvec[i]))

        dT_dL_Total = calculate_dTdL(T=float(Tvec[i]), tec=mesh[i].geometry.tec, T_env=mesh[i].geometry.T_env,
                                     ρ_slip=pvt_mixture.ρ_slip, Qm=Qm, g=g, θ=mesh[i].geometry.θ,
                                     cp_slip=pvt_mixture.cp_slip)

        Pvec[i + 1] = Pvec[i] + dP_dL_Total * mesh[i].dL
        Tvec[i + 1] = Tvec[i] + dT_dL_Total * mesh[i].dL

        MD[i + 1] = mesh[i + 1].MDf

        λLvec[i] = λL
        HLvec[i] = HL
        ρ_slip_vec[i] = pvt_mixture.ρ_slip
        μ_slip_vec[i] = pvt_mixture.μ_slip
        Pb_vec[i] = pvt.Pb
        Rs_vec[i] = pvt.Rs

    λLvec[-1] = λLvec[-2]
    HLvec[-1] = HLvec[-2]
    ρ_slip_vec[-1] = ρ_slip_vec[-2]
    μ_slip_vec[-1] = μ_slip_vec[-2]
    Pb_vec[-1] = Pb_vec[-2]
    Rs_vec[-1] = Rs_vec[-2]
    Bo_vec[-1] = Bo_vec[-2]
    ρ_oil_vec[-1] = ρ_oil_vec[-2]
    ρ_gas_vec[-1] = ρ_gas_vec[-2]
    μ_oil_vec[-1] = μ_oil_vec[-2]
    μ_gas_vec[-1] = μ_gas_vec[-2]

    return ResultsData(
        Pvec=Pvec,
        Tvec=Tvec,
        MD=MD,
        HLvec=HLvec,
        ρ_slip_vec=ρ_slip_vec,
        μ_slip_vec=μ_slip_vec,
        Pb_vec=Pb_vec,
        Rs_vec=Rs_vec,
        Bo_vec=Bo_vec,
        ρ_oil_vec=ρ_oil_vec,
        ρ_gas_vec=ρ_gas_vec,
        μ_oil_vec=μ_oil_vec,
        μ_gas_vec=μ_gas_vec,
    )
