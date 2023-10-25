from fluid_data import *


def calculate_reduced_properties(
    fd: FluidData,
    P: float,
    T: float
) -> tuple[float, float]:

    Ppr = P / fd.Ppc
    Tpr = T / fd.Tpc

    return Ppr, Tpr


def calculate_Z():
    pass


def calculate_Bg():
    pass

def calculate_ρ_gas():
    pass

