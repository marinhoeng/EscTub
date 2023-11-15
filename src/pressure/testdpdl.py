import math as m
dh = 1 / 3
e = 0.0006
Vsg = 14.318
Vm = 32.233
ρ_NS = 31.668
μ_NS = 3.698*10**-4
ρslip = 32.416
θ = 90
g = 32.2
λL = 0.556
HL = 0.573
Pfundo = 3625.94

y = λL / HL ** 2
el = e / dh
ReNS = (ρ_NS * Vm * dh) / μ_NS

dPdL_grav = (ρslip * g * m.sin(θ))*(1/144)

fn = 0.0055 * (1 + (20000 * el + 10 ** 6 / ReNS) ** (1 / 3))
if 1 < y < 1.2:
    parametro_s = m.log(2.2 * y - 1.2)
else:
    parametro_s = m.log(y) / (
                -0.0523 + (3.182 * m.log(y)) - (0.8725 * (m.log(y)) ** 2) + (0.01853 * (m.log(y)) ** 4))
fric_factor = fn * m.exp(parametro_s)
if 0 < HL < 1:
    fd = fric_factor
else:
    fd = fn

dPdL_friccao = -((fd * ρ_NS * Vm ** 2) / (2 * dh))*(1/144)

Ek = (ρslip * Vm * Vsg) / Pfundo

dPdL_Total = (dPdL_grav + dPdL_friccao) / (1. - Ek)

print(y)
print(el)
print(ReNS)
print(fric_factor)
print(dPdL_grav)
print(dPdL_friccao)
print(Ek)
print(dPdL_Total)
