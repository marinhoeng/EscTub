import math as m


def calculate_Beggs_Brill(
    ρ_oil: float,
    λL: float,
    Vsl: float,
    Vm: float,
    dh: float,
    σog: float,
    θ: float,
    g: float
) -> float:
    F_rm = Vm ** 2 / (g * dh)
    L1 = 316 * λL ** 0.302
    L2 = 0.0009252 * λL ** (-2.4684)
    L3 = 0.10 * λL ** (-1.4516)
    L4 = 0.5 * λL ** (-6.738)
    Nlv = Vsl * (ρ_oil / (g * σog)) ** 0.25

    def calculate_HL_segregado(λL: float, Nlv: float, F_rm: float, θ: float) -> float:
        a = 0.98
        b = 0.4846
        c = 0.0868

        dlinha = 0.011
        ee = -3.768
        f = 3.539
        gg = -1.614

        C = (1 - λL) * m.log(dlinha * λL ** ee * Nlv ** f * F_rm ** gg)
        ψ = 1 + C * (m.sin(1.8 * θ) - (0.333 * (m.sin(1.8 * θ)) ** 3))

        HLo_segregado = (a * λL ** b) / F_rm ** c

        if HLo_segregado < λL:
            HLo_segregado = λL

        HL_segregado = HLo_segregado * ψ

        return HL_segregado

    def calculate_HL_intermitente(λL: float, Nlv: float, F_rm: float, θ: float) -> float:
        a = 0.845
        b = 0.5352
        c = 0.0173

        dlinha = 2.960
        ee = 0.305
        f = -0.4473
        gg = 0.0978

        C = (1 - λL) * m.log(dlinha * (λL ** ee) * (Nlv ** f) * (F_rm ** gg))
        ψ = 1 + (C * (m.sin(1.8 * θ) - 0.333 * (m.sin(1.8 * θ)) ** 3))

        HLo_intermitente = (a * λL ** b) / (F_rm ** c)

        if HLo_intermitente < λL:
            HLo_intermitente = λL

        HL_intermitente = HLo_intermitente * ψ
        return HL_intermitente

    def calculate_HL_distribuido(λL: float, F_rm: float) -> float:
        a = 1.065
        b = 0.5824
        c = 0.0609

        ψ = 1

        HLo_distribuido = (a * λL ** b) / F_rm ** c

        if HLo_distribuido < λL:
            HLo_distribuido = λL

        HL_distribuido = HLo_distribuido * ψ

        return HL_distribuido

    # segregado
    # intermitente
    # distribuido
    # transicao (segregado e intermitente)

    if (λL < 0.01 and F_rm < L1) or (λL >= 0.01 and F_rm < L2):  # segregado

        HL = calculate_HL_segregado(λL=λL, Nlv=Nlv, F_rm=F_rm, θ=θ)

    elif ((0.01 <= λL < 0.4) and (L3 <= F_rm <= L1)) or ((λL >= 0.4) and (L3 <= F_rm <= L4)):  # intermitente

        HL = calculate_HL_intermitente(λL=λL, Nlv=Nlv, F_rm=F_rm, θ=θ)

    elif (λL < 0.4 and F_rm >= L1) or (λL >= 0.4 and F_rm > L4):  # distribuido

        HL = calculate_HL_distribuido(λL=λL, F_rm=F_rm)

    elif λL >= 0.01 and (L2 <= F_rm <= L3):  # transicao

        A = (L3 - F_rm) / (L3 - L2)

        HL_s = calculate_HL_segregado(λL=λL, Nlv=Nlv, F_rm=F_rm, θ=θ)
        HL_i = calculate_HL_intermitente(λL=λL, Nlv=Nlv, F_rm=F_rm, θ=θ)

        HL_transicao = A * HL_s + (1 - A) * HL_i

        HL = HL_transicao

    else:
        raise ValueError("BB failed.")

    if HL > (1. - 1e-6):
        raise ValueError("BB failed.")

    return HL
