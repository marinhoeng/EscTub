import numpy as np

# Dados de entrada
dre = np.array([0.3490, 0.3410, 0.1956, 0.1902, 0.1896, 0.1890])
dri = np.array([0.3410, 0.1956, 0.1902, 0.1896, 0.1890, 0.1524])
dfe = np.array([0.3432, 0.3352, 0.2098, 0.2044, 0.2038, 0.2032])
dfi = np.array([0.3352, 0.2098, 0.2044, 0.2038, 0.2032, 0.1524])
d1e = np.array([0.3175, 0.2413, 0.2159, 0.1397])
d1i = np.array([0.2413, 0.2159, 0.1397, 0.1143])
d2e = np.array([0.3556, 0.3175, 0.2413, 0.2159, 0.1397])
d2i = np.array([0.3175, 0.2413, 0.2159, 0.1397, 0.1143])
d3e = np.array([0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397])
d3i = np.array([0.3556, 0.3175, 0.2413, 0.2159, 0.1397, 0.1143])
d4e = np.array([0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397])
d4i = np.array([0.3556, 0.3175, 0.2413, 0.2159, 0.1397, 0.1143])
d5e = np.array([0.6858, 0.508, 0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397])
d5i = np.array([0.508, 0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397, 0.1143])
d6e = np.array([0.9144, 0.762, 0.6858, 0.508, 0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397])
d6i = np.array([0.762, 0.6858, 0.508, 0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397, 0.1143])


k_values = np.array([0.2250, 0.1680, 0.2250, 0.2250, 0.2940, 45.0])
k_values_1 = np.array([0.9, 45, 0.3, 45])
k_values_2 = np.array([45, 0.9, 45, 0.3, 45])
k_values_3 = np.array([0.9, 45, 0.58, 45, 0.3, 45])
k_values_4 = np.array([0.58, 45, 0.58, 45, 0.3, 45])
k_values_5 = np.array([0.9, 45, 0.58, 45, 0.58, 45, 0.3, 45])
k_values_6 = np.array([0.9, 45, 0.9, 45, 0.58, 45, 0.58, 45, 0.3, 45])

def tec_riser(dre, dri, k_values):
    lnr = np.log(dre / dri)
    lnrK = lnr / k_values
    somatorior = np.sum(lnrK)
    Keqr = np.log(dre[0] / dri[-1]) / somatorior
    tec_r = ((2 * np.pi * Keqr) / np.log((dre[0] / 2) / (dri[-1] / 2)))
    return tec_r

def tec_flowline(dfe, dfi, k_values):
    lnf = np.log(dfe / dfi)
    lnfK = lnf / k_values
    somatoriof = np.sum(lnfK)
    Keqf = np.log(dfe[0] / dfi[-1]) / somatoriof
    tec_f = ((2 * np.pi * Keqf) / np.log((dfe[0] / 2) / (dfi[-1] / 2)))
    return tec_f

def tec_poco_1(d1e,d1i, k_values_1):
    ln1 = np.log(d1e / d1i)
    ln1K = ln1 / k_values_1
    somatorio1 = np.sum(ln1K)
    Keq1 = np.log(d1e[0] / d1i[-1]) / somatorio1
    tec_1 = ((2 * np.pi * Keq1) / np.log((d1e[0] / 2) / (d1i[-1] / 2)))
    return tec_1

def tec_poco_2(d2e, d2i, k_values_2):
    ln2 = np.log(d2e / d2i)
    ln2K = ln2 / k_values_2
    somatorio2 = np.sum(ln2K)
    Keq2 = np.log(d2e[0] / d2i[-1]) / somatorio2
    tec_2 = ((2 * np.pi * Keq2) / np.log((d2e[0] / 2) / (d2i[-1] / 2)))
    return tec_2

def tec_poco_3(d3e, d3i, k_values_3):
    ln3 = np.log(d3e / d3i)
    ln3K = ln3 / k_values_3
    somatorio3 = np.sum(ln3K)
    Keq3 = np.log(d3e[0] / d3i[-1]) / somatorio3
    tec_3 = ((2 * np.pi * Keq3) / np.log((d3e[0] / 2) / (d3i[-1] / 2)))
    return tec_3

def tec_poco_4(d4e, d4i, k_values_4):
    ln4 = np.log(d4e / d4i)
    ln4K = ln4 / k_values_4
    somatorio4 = np.sum(ln4K)
    Keq4 = np.log(d4e[0] / d4i[-1]) / somatorio4
    tec_4 = ((2 * np.pi * Keq4) / np.log((d4e[0] / 2) / (d4i[-1] / 2)))
    return tec_4

def tec_poco_5(d5e, d5i, k_values_5):
    ln5 = np.log(d5e / d5i)
    ln5K = ln5 / k_values_5
    somatorio5 = np.sum(ln5K)
    Keq5 = np.log(d5e[0] / d5i[-1]) / somatorio5
    tec_5 = ((2 * np.pi * Keq5) / np.log((d5e[0] / 2) / (d5i[-1] / 2)))
    return tec_5

def tec_poco_6(d6e, d6i, k_values_6):
    ln6 = np.log(d6e / d6i)
    ln6K = ln6 / k_values_6
    somatorio6 = np.sum(ln6K)
    Keq6 = np.log(d6e[0] / d6i[-1]) / somatorio6
    tec_6 = ((2 * np.pi * Keq6) / np.log((d6e[0] / 2) / (d6i[-1] / 2)))
    return tec_6

tec_r = tec_riser(dre, dri, k_values)
tec_f = tec_flowline(dfe, dfi, k_values)

print("TEC Riser:", tec_r)
print("TEC Flowline:", tec_f)

tec_p1 = tec_poco_1(d1e, d1i, k_values_1)
tec_p2 = tec_poco_2(d2e, d2i, k_values_2)
tec_p3 = tec_poco_3(d3e, d3i, k_values_3)
tec_p4 = tec_poco_4(d4e, d4i, k_values_4)
tec_p5 = tec_poco_5(d5e, d5i, k_values_5)
tec_p6 = tec_poco_6(d6e, d6i, k_values_6)

print("TEC Poço 1:", tec_p1)
print("TEC Poço 2:", tec_p2)
print("TEC Poço 3:", tec_p3)
print("TEC Poço 4:", tec_p4)
print("TEC Poço 5:", tec_p5)
print("TEC Poço 6:", tec_p6)




