import numpy as np


def calculate_dTdL(T: float, tec: float, T_env: float, ρ_slip: float,
                   Qm: float, g: float, θ: float, cp_slip: float) -> float:

    dT_dL = (-tec * (T - T_env) - (ρ_slip * Qm * g * np.sin(θ))) / (ρ_slip * Qm * cp_slip)

    return dT_dL