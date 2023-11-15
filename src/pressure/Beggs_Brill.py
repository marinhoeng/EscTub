import math as m
from Flow_Velocity import FlowVelocity


def calculate_Beggs_Brill(fv: FlowVelocity) -> float:
    ρL = 0.
    λL = fv.λL
    Vsl = fv.Vsl
    Vm = fv.Vm

    F_rm = Vm ** 2 / (g * dh)
    L1 = 316 * λL ** 0.302
    L2 = 0.0009252 * λL ** (-2.4684)
    L3 = 0.10 * λL ** (-1.4516)
    L4 = 0.5 * λL ** (-6.738)

    Nlv = Vsl * (ρL / (g * σL))

    if (λL < 0.4 and F_rm >= L1) or (λL >= 0.4 and F_rm > L4):
        Padrao = "Distribuido"
        C = 0
        ψ = 1
        a = 1.065
        b = 0.5824
        c = 0.0609
        HLo = (a * λL ** b) / F_rm ** c
        HL = HLo * ψ

    elif (λL < 0.01 and F_rm < L1) or (λL >= 0.01 and F_rm < L2):
        Padrao = "Segregado"
        a = 0.98
        b = 0.4846
        c = 0.0868
        dlinha = 0.011
        ee = -3.768
        f = 3.539
        gg = -1.614
        C = (1 - λL) * m.log(dlinha * λL ** ee * Nlv ** f * F_rm ** gg)
        if C < 0:
            C = 0
            ψ = 1
        else:
            ψ = 1 + (C * m.sin(1.8 * θ) - 0.333 * (m.sin(1.8 * θ)) ** 3)
        HLo = (a * λL ** b) / F_rm ** c
        HL = HLo * ψ

    elif ((0.01 <= λL < 0.4) and (L3 <= F_rm <= L1)) or (λL >= 0.4 and (L3 <= F_rm <= L4)):
        Padrao = "Intermitente"
        a = 0.845
        b = 0.5352
        c = 0.0173
        dlinha = 2.960
        ee = 0.305
        f = -0.4473
        gg = 0.0978
        C = (1 - λL) * m.log(dlinha * λL ** ee * Nlv ** f * F_rm ** gg)
        if C < 0:
            C = 0
            ψ = 1
        else:
            ψ = 1 + (C * m.sin(1.8 * θ) - 0.333 * (m.sin(1.8 * θ)) ** 3)
        HLo = (a * λL ** b) / F_rm ** c
        HL = HLo * ψ

    elif λL >= 0.01 and (L2 <= F_rm <= L3):
        Padrao = "Transição"
        A = (L3 - F_rm) / (L3 - L2)

        # Hl - Segregado
        a = 0.98
        b = 0.4846
        c = 0.0868
        dlinha = 0.011
        ee = -3.768
        f = 3.539
        gg = -1.614
        C = (1 - λL) * m.log(dlinha * λL ** ee * Nlv ** f * F_rm ** gg)
        if C < 0:
            C = 0
            ψ = 1
        else:
            ψ = 1 + (C * m.sin(1.8 * θ) - 0.333 * (m.sin(1.8 * θ)) ** 3)
        HLo = (a * λL ** b) / F_rm ** c
        HL_s = HLo * ψ

        # Hl - Intermitente
        a = 0.845
        b = 0.5352
        c = 0.0173
        dlinha = 2.960
        ee = 0.305
        f = -0.4473
        gg = 0.0978
        C = (1 - λL) * m.log(dlinha * λL ** ee * Nlv ** f * F_rm ** gg)
        if C < 0:
            C = 0
            ψ = 1
        else:
            ψ = 1 + (C * m.sin(1.8 * θ) - 0.333 * (m.sin(1.8 * θ)) ** 3)
        HLo = (a * λL ** b) / F_rm ** c
        HL_i = HLo * ψ

        # HL - Transição
        HL = A * HL_s + (1 - A) * HL_i

    return HL


result = calculate_Beggs_Brill()
print("HL =", result)

# Giovanna_test