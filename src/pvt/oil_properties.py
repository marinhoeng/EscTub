import math as m
from pvt.gas_properties import calculate_Bg
from pvt.fluid_data import Unit, FluidData


def calculate_Rs(fd: FluidData, P: float, T: float, Pb: float | None = None) -> float:
    T_F = Unit.mCalc_Conv_Temperature(T, 'K', 'F')
    P_psi = Unit.mCalc_Conv_Pressure(P, 'Pa', 'psi')

    if Pb is None:
        Pb = calculate_Pb(fd=fd, T=T)

    if P >= Pb:
        return fd.RGO

    # Petrosky-Farshad's Correlation
    A = (7.916 * 10 ** -4) * (fd.API ** 1.541) - (4.561 * 10 ** -5) * (T_F ** 1.3911)
    Rs = (((P_psi / 112.727) + 12.34) * (fd.dg ** 0.8439) * (10 ** A)) ** 1.73184  # SCF/STB

    Rs = Unit.mCalc_Conv_Volration(Rs, 'scf/stb', 'm3/m3')

    return Rs


def calculate_Pb(fd: FluidData, T: float) -> float:
    Rsb = Unit.mCalc_Conv_Volration(fd.RGO, 'm3/m3', 'scf/stb')
    T_F = Unit.mCalc_Conv_Temperature(T, 'K', 'F')

    # Petrosky-Farshad's Correlation
    A = (7.916 * 10 ** -4) * (fd.API ** 1.541) - (4.561 * 10 ** -5) * (T_F ** 1.3911)

    Pb = ((112.727 * (Rsb ** 0.577421)) / ((fd.dg ** 0.8439) * (10 ** A))) - 1391.051

    Pb = Unit.mCalc_Conv_Pressure(Pb, 'psi', 'Pa')

    return Pb


def calculate_Bo(fd: FluidData, P: float, T: float, Rs: float | None = None, Pb: float | None = None) -> float:
    if Pb is None:
        Pb = calculate_Pb(fd=fd, T=T)
    if Rs is None:
        Rs = calculate_Rs(fd=fd, P=P, T=T)

    if P > Pb:
        Co = calculate_Co(fd=fd, P=P, T=T)
        T_F = Unit.mCalc_Conv_Temperature(T, 'K', 'F')
        P = Unit.mCalc_Conv_Pressure(P, 'pa', 'psi')
        Pb = Unit.mCalc_Conv_Pressure(Pb, 'pa', 'psi')
        Rsb = Unit.mCalc_Conv_Volration(fd.RGO, 'm3/m3', 'scf/stb')

        # Petrosky-Farshad's Correlation
        Bob = 1.0113 + 7.2046 * 10 ** -5 * (
                ((Rsb ** 0.3738) * ((fd.dg ** 0.2914) / (fd.do ** 0.6265)) + 0.24626 * (T_F ** 0.5371)) ** 3.0936)
        Bo_subsat = Bob * m.exp(-Co * (P - Pb))
        Bo = Unit.mCalc_Conv_Volration(Bo_subsat, 'bbl/STB', 'm3/m3')
        return Bo

    else:
        T_F = Unit.mCalc_Conv_Temperature(T, 'K', 'F')
        Rs_scfSTB = Unit.mCalc_Conv_Volration(Rs, 'm3/m3', 'scf/stb')

        # Petrosky-Farshad's Correlation
        Bo_sat_bblSTB = 1.0113 + 7.2046 * 10 ** -5 * (
                ((Rs_scfSTB ** 0.3738) * ((fd.dg ** 0.2914) / (fd.do ** 0.6265)) + 0.24626 * (T_F ** 0.5371)) ** 3.0936)

        Bo = Unit.mCalc_Conv_Volration(Bo_sat_bblSTB, 'bbl/STB', 'm3/m3')
        return Bo


def calculate_Co(fd: FluidData, P: float, T: float, Pb: float | None = None) -> float:
    """

    :param fd:
        Object of a FluidData. [-]

    :param P:
        Pressure. [Pa]

    :param T:
        Temperature. [K]

    :param Pb:
        Bubble pressure. [Pa]

    :return:
        Oil compressibility at saturation stage. [Pa^-1]
    """
    if Pb is None:
        Pb = calculate_Pb(fd=fd, T=T)

    if P >= Pb:  # subsat
        P_psi = Unit.mCalc_Conv_Pressure(P, 'pa', 'psi')
        T_F = Unit.mCalc_Conv_Temperature(T, 'K', 'F')
        Rsb = Unit.mCalc_Conv_Volration(fd.RGO, 'm3/m3', 'scf/stb')

        Co_subsat = 1.705 * 10 ** -7 * (Rsb ** 0.69357) * (fd.dg ** 1.1885) * (fd.API ** 0.3272) * (
                T_F ** 0.6729) * (P_psi ** -0.5906)
        Co = Unit.mCalc_Conv_Comp(Co_subsat, 'psi-1', 'pa-1')
        return Co

    Bg = calculate_Bg(fd=fd, P=P, T=T)

    Bo = calculate_Bo(fd=fd, P=P, T=T)

    δ = 1e-4

    Rs_up = calculate_Rs(fd=fd, P=P + δ, T=T, Pb=Pb)
    Rs_down = calculate_Rs(fd=fd, P=P - δ, T=T, Pb=Pb)

    Bo_up = calculate_Bo(fd=fd, P=P, T=T, Rs=Rs_up, Pb=Pb)
    Bo_down = calculate_Bo(fd=fd, P=P, T=T, Rs=Rs_down, Pb=Pb)

    dBo_dP = (Bo_up - Bo_down) / (2. * δ)
    dRs_dP = (Rs_up - Rs_down) / (2. * δ)

    Co = (-1. / Bo) * dBo_dP + (Bg / Bo) * dRs_dP  # pa-1

    return Co


def calculate_ρ_oil(fd: FluidData, P: float, T: float, Pb: float | None = None, Rs: float | None = None) -> float:
    Co = calculate_Co(fd=fd, P=P, T=T)
    Bo = calculate_Bo(fd=fd, P=P, T=T, Pb=Pb)
    if Pb is None:
        Pb = calculate_Pb(fd=fd, T=T)

    if P > Pb:
        Rsb = Unit.mCalc_Conv_Volration(fd.RGO, 'm3/m3', 'scf/stb')

        ρ_ob = ((62.4 * fd.do) + (0.0136 * Rsb * fd.dg)) / Bo
        ρ_oil = ρ_ob * m.exp(Co * (P - Pb))
        ρ_oil = Unit.mCalc_Conv_Density(ρ_oil, 'lb/ft3', 'kg/m3')

    else:
        if Rs is None:
            Rs = calculate_Rs(fd=fd, P=P, T=T)

        Rs_scf_stb = Unit.mCalc_Conv_Volration(Rs, 'm3/m3', 'scf/stb')

        ρ_oil = ((62.4 * fd.do) + (0.0136 * Rs_scf_stb * fd.dg)) / Bo
        ρ_oil = Unit.mCalc_Conv_Density(ρ_oil, 'lb/ft3', 'kg/m3')

    return ρ_oil


def calculate_μ_oil(fd: FluidData, P: float, T: float, Pb: float | None = None) -> float:
    T_F = Unit.mCalc_Conv_Temperature(T, 'K', 'F')
    P_psi = Unit.mCalc_Conv_Pressure(P, 'pa', 'psi')
    Pb_psi = Unit.mCalc_Conv_Pressure(Pb, 'pa', 'psi')

    if Pb is None:
        Pb = calculate_Pb(fd=fd, T=T)

    Rs_scf_stb = Unit.mCalc_Conv_Volration(calculate_Rs(fd=fd, P=P, T=T, Pb=Pb), 'm3/m3', 'scf/stb')

    # Beggs-Robinson's Correlation
    a = 10 ** (3.0324 - 0.02023 * fd.API)
    μ_od = 10 ** (a * (T_F ** (-1.163))) - 1  # cP

    A = 10.715 * (Rs_scf_stb + 100) ** (-0.515)
    B = 5.44 * (Rs_scf_stb + 150) ** (-0.338)
    μ_oil_sat = A * μ_od ** B  # cP

    if P <= Pb:
        return Unit.mCalc_Conv_Viscosity(μ_oil_sat, 'cp', 'Pa·s')

    A = (2.6 * P_psi ** 1.187) * m.exp(-11.513 - 8.98e-5 * P_psi)
    μ_oil_subsat = μ_oil_sat * (P_psi / Pb_psi) ** A  # cP

    return Unit.mCalc_Conv_Viscosity(μ_oil_subsat, 'cp', 'Pa·s')


def calculate_cp_oil(fd: FluidData, P: float, T: float) -> float:
    return 1716.6
