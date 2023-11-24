import math as m


def calculate_y(HL: float, λL: float) -> float:
    return λL / HL ** 2


def calculate_Re_NS(ρ_NS: float, Vm: float, dh: float, μ_NS: float) -> float:
    return (ρ_NS * Vm * dh) / μ_NS


def calculate_fn(Rens: float, εr: float) -> float:
    return 0.0055 * (1 + (20000 * εr + 10 ** 6 / Rens) ** (1 / 3))


def calculate_fric_factor(Rens: float, y: float, εr: float) -> float:
    if 1 < y < 1.2:
        parametro_s = m.log(2.2 * y - 1.2)
    else:
        parametro_s = m.log(y) / (
                -0.0523 + (3.182 * m.log(y)) - (0.8725 * (m.log(y)) ** 2) + (0.01853 * (m.log(y)) ** 4))

    fn = calculate_fn(Rens=Rens, εr=εr)

    ftp = fn * m.exp(parametro_s)

    return ftp


def calculate_dPdL_grav(ρ_slip: float, g: float, θ: float) -> float:
    return ρ_slip * g * m.sin(θ)


def calculate_dPdL_friccao(HL: float, Rens: float, y: float, εr: float, Vm: float, ρ_NS: float, dh: float) -> float:

    if 0 < HL < 1:
        # Two Phase
        fd = calculate_fric_factor(Rens=Rens, y=y, εr=εr)
    else:
        # Single Phase
        fd = calculate_fn(Rens=Rens, εr=εr)

    dPdL_friccao = (fd * ρ_NS * Vm ** 2) / (2 * dh)

    return dPdL_friccao


def calculate_Pwf(P_res: float, IP: float, Q_sc: float) -> float:

    Pwf = P_res - (Q_sc/IP)

    return Pwf


def calculate_dPdL_Total(HL: float, Rens: float, y: float, εr: float, ρ_NS: float, ρ_slip: float, g: float,
                         θ: float, Vm: float, Vsg: float, dh: float, P: float) -> float:

    dPdL_grav = calculate_dPdL_grav(ρ_slip=ρ_slip, g=g, θ=θ)

    dPdL_friccao = calculate_dPdL_friccao(HL=HL, Rens=Rens, y=y, εr=εr, Vm=Vm, ρ_NS=ρ_NS, dh=dh)

    if 0 < HL < 1:
        Ek = (ρ_slip * Vm * Vsg) / P
        if abs(Ek - 1.) < 1e-3:
            Ek = 0.999
    else:
        Ek = 0.

    dPdL_Total = (-dPdL_grav - dPdL_friccao) / (1. - Ek)

    return dPdL_Total
