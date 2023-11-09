import math as m
from fluid_data import FluidData
from Beggs_Brill import calculate_Beggs_Brill
from Flow_Velocity import flow_velocity_in_situ


def calculate_rugosidade() -> float:
    el = e / dh

    return el


def calculate_Re_NS(fv: flow_velocity_in_situ) -> float:
    ReNS = (ρNS * fv.Vm * dh) / μ_NS

    return ReNS


def calculate_dPdL_grav() -> float:
    dPdL_grav = ρslip * g * m.sin(θ)

    return dPdL_grav


def calculate_fn(ReNS: float, el: float) -> float:
    # rugosidade relativa

    fn = 0.0055 * (1 + (20000 * el + 10 ** 6 / ReNS) ** (1 / 3))

    return fn


def calculate_fric_factor(ReNS: float, y: float, el: float) -> float:
    if 1 < y < 1.2:
        parametro_s = m.log(2.2 * y - 1.2)
    else:
        parametro_s = m.log(y) / (
                    -0.0523 + (3.182 * m.log(y)) - (0.8725 * (m.log(y)) ** 2) + (0.01853 * (m.log(y)) ** 4))

    fn = calculate_fn(ReNS, el)

    fric_factor = fn * m.exp(parametro_s)

    return fric_factor


def calculate_dPdL_friccao(fv: flow_velocity_in_situ) -> float:
    dPdL_friccao = - (fd * ρ_NS * fv.Vm ** 2) / (2 * dh)

    return dPdL_friccao


def calculate_dPdL_Total(fv: flow_velocity_in_situ) -> float:
    Ek = (ρslip * fv.Vm * fv.Vsg) / Pfundo

    dPdL_Total = (dPdL_grav + dPdL_friccao) / (1. - Ek)

    return dPdL_Total

# Giovanna_test