# Input data
import numpy as np

from pressure.Flow_Velocity import calculate_flow_insitu
from pressure.dPdL import calculate_Re_NS
from pvt.fluid_data import FluidData
from pvt.pvt_properties import PVTProperties
from _tests.test_mesh import base_case_study as case
from mesh.mesh import building_mesh
from pvt.pvt_properties import calculate_pvt_properties

g = 9.81


def test_flow_analysis(case) -> None:
    mesh = building_mesh(data=case)

    sec_number = len(mesh)

    Pvec = np.zeros(sec_number)
    Tvec = np.zeros(sec_number)

    fd = FluidData()

    fd = fd.set_fluid_data(API=case.API, dg=case.dg, RGO=case.RGO)

    # Pwf = calculate_pwf()

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

        Rens = calculate_Re_NS(ρ_NS=pvt.ρ_NS, Vm=Vm, dh=mesh[i].geometry.dh, μ_NS=pvt.μ_NS)

        dh = mesh[i].geometry.dh

    assert 1 == 1
