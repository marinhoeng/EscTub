import math as m
from pvt.fluid_data import Unit, FluidData


def calculate_reduced_properties(fd: FluidData, P: float, T: float) -> tuple[float, float]:
    Ppr = P / fd.Ppc
    Tpr = T / fd.Tpc

    return Ppr, Tpr


def calculate_Z(fd: FluidData, P: float, T: float) -> float:
    Ppr, Tpr = calculate_reduced_properties(fd=fd, P=P, T=T)

    # Z Factor - Shell's Correlation
    Za = -0.101 - 0.36 * (Tpr + 1.3868) * ((Tpr - 0.919) ** 0.5)
    Zb = 0.21 + (0.04275 / (Tpr - 0.65))
    Zc = 0.6222 - 0.224 * Tpr
    Zd = (0.0657 / (Tpr - 0.86)) - 0.037
    Ze = 0.32 * m.exp(-19.53 * (Tpr - 1))
    Zf = 0.122 * m.exp(-11.3 * (Tpr - 1))
    Zg = Ppr * (Zc + Zd * Ppr + Ze * (Ppr ** 4))
    Z = Za + Zb * Ppr + (1 - Za) * m.exp(-Zg) - Zf * ((Ppr / 10) ** 4)

    return Z


def calculate_Bg(
    fd: FluidData,
    P: float,
    T: float,
    Z: float | None = None
) -> float:
    if Z is None:
        Z = calculate_Z(fd=fd, P=P, T=T)

    Bg = (fd.Psc / fd.Tsc) * (Z * T) / P

    return Bg


def calculate_ρ_gas(
    fd: FluidData,
    P: float,
    T: float,
    Z: float | None = None
) -> float:
    if Z is None:
        Z = calculate_Z(fd=fd, P=P, T=T)

    ρ_gas = (P * fd.MMg) / (Z * fd.R * T)  # kg/m3

    return ρ_gas


def calculate_Cg(fd: FluidData, P: float, T: float, Z: float | None = None) -> float:

    if Z is None:
        Z = calculate_Z(fd=fd, P=P, T=T)

    δ = 1e-3
    Z_up = calculate_Z(fd=fd, P=P + δ, T=T)
    Z_down = calculate_Z(fd=fd, P=P - δ, T=T)

    dZ_dP = (Z_up - Z_down) / (2. * δ)

    Cg = (1./P) - 1./Z * dZ_dP  # Pa-1

    return Cg


def calculate_μ_gas(fd: FluidData, P: float, T: float, Z: float | None = None) -> float:

    ρ_gas = calculate_ρ_gas(fd=fd, P=P, T=T, Z=Z)  # kg/m3

    ρ_gas_lbft3 = Unit.mCalc_Conv_Density(ρ_gas, 'kg/m3', 'lb/ft3')
    Mw_gas = fd.MMg * 1000  # lb/mol
    T_R = Unit.mCalc_Conv_Temperature(T, 'K', 'R')

    # Lee's Correlation
    xv = 3.448 + (986.4 / T_R) + 0.01009 * Mw_gas
    yv = 2.4 - 0.2 * xv
    kv = ((9.379 + 0.01607 * Mw_gas) * (T_R ** 1.5)) / (209.2 + 19.26 * Mw_gas +  T_R )

    μ_gas_cp = (1e-4 * kv) * m.exp(xv * ((ρ_gas_lbft3 / 62.4) ** yv))

    μ_gas = Unit.mCalc_Conv_Viscosity(μ_gas_cp, 'cp','Pa·s')

    return μ_gas


def calculate_cp_gas(fd: FluidData, P: float, T: float) -> float:
    return 2206.4

