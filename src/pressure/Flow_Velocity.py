import math as m
from fluid_data import FluidData
from oil_properties import (calculate_Pb,
                            calculate_Rs,
                            calculate_Bg,
                            calculate_Bosat,
                            calculate_Bosubsat
                            )


class flow_velocity_in_situ:
    def __init__(self, Qo, Qg, Ql, Vsl, Vsg, Vm, λL):
        self.Qo: float = Qo
        self.Qg: float = Qg
        self.Ql: float = Ql
        self.Vsl: float = Vsl
        self.Vsg: float = Vsg
        self.Vm: float = Vm
        self.λL: float = λL


def calculate_flow_velocity_in_situ(fd: FluidData, Qlsc: float, P: float, T: float, Z: float) -> flow_velocity:
    Pb = calculate_Pb(fd=fd, P=P, T=T)
    Rs = calculate_Rs(fd=fd, P=P, T=T)
    Bg = calculate_Bg(fd=fd, P=P, T=T, Z=Z)

    Qostd = Qlsc
    Ap = (m.pi * fd.dh ** 2) / 4

    if P > Pb:
        Qo = Qostd * Bosat
        Ql = Qo
        Vsl = Ql / Ap
        λL = 1
        Vsg = 0.
        Vm = Vsl
        Qg = 0.

    else:
        Qo = Qostd * Bosubsat
        Ql = Qo
        Vsl = Ql / Ap
        Qgsc = fd.RGO * Qlsc  # RGO = RGL and BSW = 0

        Qg = (fd.RGO - Rs) * Qostd * Bg  # For RSW = 0

        Vsg = Qg / Ap
        Vm = Vsl + Vsg
        λL = Vsl / Vm

    return flow_velocity(Qo, Qg, Qgsc, Ql, Vsl, Vsg, Vm, λL)

# Giovanna_test