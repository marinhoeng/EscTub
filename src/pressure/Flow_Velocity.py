import math as m

from src.mesh.mesh import MeshData, InputData
from src.pvt.pvt_properties import PVTProperties


def calculate_flow_insitu(
    data: InputData,
    dh: float,
    pvt: PVTProperties,
    P: float,
    Pb: float
) -> tuple[float, float, float, float, float]:
    Ap = (m.pi * dh ** 2) / 4

    Vsg = 0.
    Qg = 0.
    if P < Pb:
        Qg = (data.RGO - pvt.Rs) * data.Q_sc * pvt.Bg
        Vsg = Qg / Ap

    Qo = data.Q_sc * pvt.Bo
    Vsl = Qo / Ap
    Vm = Vsl + Vsg
    λL = Vsl / Vm
    Qm = Qo + Qg

    return Qm, Vm, Vsl, Vsg, λL
