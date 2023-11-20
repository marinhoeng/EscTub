import numpy as np
from mesh import Mesh
from Beggs_Brill import calculate_Beggs_Brill
from pvt_properties import PVTProperties
from Flow_Velocity import FlowVelocity



def calculate_dTdL(T: float, TEC: float, T_env: float, ρ_slip: float, Qm: float, g: float, θ: float, cp_slip: float)\
        -> float:

    dT_dL = (-TEC * (T - T_env) - (ρ_slip * Qm * g * np.sin(θ))) / (ρ_slip * Qm * cp_slip)

    return dT_dL

