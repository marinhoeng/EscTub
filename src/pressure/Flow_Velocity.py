import math as m
from pvt.fluid_data import FluidData
from pvt.oil_properties import (calculate_Pb,
                                calculate_Rs,
                                calculate_Bg,
                                calculate_Bo)


class FlowVelocity:
    def __init__(self, Qo, Qg, Qgsc, Ql, Vsl, Vsg, λL):
        self.Qo = Qo
        self.Qg = Qg
        self.Qgsc = Qgsc
        self.Ql = Ql
        self.Vsl = Vsl
        self.Vsg = Vsg
        self.Vm = Vsl + Vsg
        self.λL = λL


def calculate_flow_velocity(fd: FluidData, Qlsc: float, P: float, T: float, Z: float) -> FlowVelocity:
    Pb = calculate_Pb(fd=fd, P=P, T=T)
    Rs = calculate_Rs(fd=fd, P=P, T=T)
    Bg = calculate_Bg(fd=fd, P=P, T=T, Z=Z)
    Bo = calculate_Bo(fd=fd, P=P, T=T, Rs=Rs, Pb=Pb)

    Qostd = Qlsc
    Ap = (m.pi * fd.dh ** 2) / 4
    Qo = Qostd * Bo

    if P > Pb:
        Vsl = Qo / Ap
        λL = 1.
        Vsg = 0.
        Qg = 0.
        Qgsc = 0.
    else:
        Vsl = Qo / Ap
        Qgsc = fd.RGO * Qlsc
        Qg = (fd.RGO - Rs) * Qostd * Bg
        Vsg = Qg / Ap
        λL = Vsl / (Vsl + Vsg)

    return FlowVelocity(Qo, Qg, Qgsc, Qo, Vsl, Vsg, λL)

# Giovanna_test
