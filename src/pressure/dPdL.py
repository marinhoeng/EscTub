import math as m
from pvt.fluid_data import FluidData
from Beggs_Brill import calculate_Beggs_Brill
from Flow_Velocity import FlowVelocity


def calculate_y(fv: FlowVelocity) -> float:
    HL = calculate_Beggs_Brill(fv=fv)
    y = fv.λL / HL ** 2
    return y


def calculate_rugosidade() -> float:
    el = e / dh

    return el


def calculate_Re_NS(fv: FlowVelocity) -> float:
    ReNS = (ρ_NS * fv.Vm * dh) / μ_NS

    return ReNS


def calculate_dPdL_grav() -> float:
    dPdL_grav = ρ_slip * g * m.sin(θ)

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

    fn = calculate_fn(ReNS=ReNS, el=el)

    ftp = fn * m.exp(parametro_s)

    return ftp


def calculate_dPdL_friccao(fv: FlowVelocity, ReNS: float, y: float, el: float, ρ_NS: float) -> float:
    HL = calculate_Beggs_Brill(fv=fv)

    if 0 < HL < 1:
        fd = calculate_fric_factor(ReNS=ReNS, y=y, el=el)
    else:
        fd = calculate_fn(ReNS=ReNS, el=el)

    dPdL_friccao = - (fd * ρ_NS * fv.Vm ** 2) / (2 * dh)

    return dPdL_friccao


def calculate_dPdL_Total(fv: FlowVelocity, ReNS: float, y: float, el: float, ρ_NS: float) -> float:
    dPdL_grav = calculate_dPdL_grav()
    dPdL_friccao = calculate_dPdL_friccao(fv=fv, ReNS=ReNS, y=y, el=el, ρ_NS=ρ_NS)
    HL = calculate_Beggs_Brill(fv=fv)

    if 0 < HL < 1:
        Ek = (ρ_slip * fv.Vm * fv.Vsg) / Pfundo
        if abs(Ek - 1.) < 1e-3:
            Ek = 0.999
    else:
        Ek = 0.

    dPdL_Total = (dPdL_grav + dPdL_friccao) / (1. - Ek)

    return dPdL_Total

# Giovanna_test
