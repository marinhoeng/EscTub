import numpy as np
from attrs import define
from numpy.typing import NDArray


@define(frozen=True)
class tec_section:
    # External diameter [m].
    de: NDArray[np.float64]
    # Internal diameter [m].
    di: NDArray[np.float64]
    # Layer number [-].
    Nl: int
    # Thermal conductivity [W/m·K].
    k_values: NDArray[np.float64]
    # Initial position [m].
    mdi: float
    # Final position [m].
    mdf: float

    def __attrs_post_init__(self):
        section_properties = [
            "de",
            "di",
            "k_values",
        ]

        if not all(self.Nl == len(getattr(self, prop)) for prop in section_properties):
            raise ValueError(
                "Filled properties size don't match with layer number when checking section data."
            )

        if self.mdf <= self.mdi or self.mdi < 0 or self.mdf < 0:
            raise ValueError("Filled positions are not inconsistent.")


def calculate_tec_section(sec: tec_section) -> float:
    ln_rk = [np.log(sec.de[i] / sec.di[i]) / sec.k_values[i] for i in range(sec.Nl)]

    Keq = np.log(sec.de[0] / sec.di[-1]) / np.sum(ln_rk)

    sec_tec = (2 * np.pi * Keq) / np.log((sec.de[0] / 2) / (sec.di[-1] / 2))

    return sec_tec
