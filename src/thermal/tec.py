import numpy as np
import pytest
from attrs import define
from numpy.typing import NDArray


@define(frozen=True)
class section:
    # External diameter [m].
    de: NDArray[np.float64]
    # Internal diameter [m].
    di: NDArray[np.float64]
    # Layer number [-].
    Nl: int
    # Thermal conductivity [W/m·K].
    k_values: NDArray[np.float64]

    def __attrs_post_init__(self):
        section_properties = [
            "de",
            "di",
            "k_values",
        ]

        if not all(self.Nl == len(getattr(self, prop)) for prop in section_properties):
            raise ValueError(
                "Filled properties size don't match with layer number when checking section data"
            )


def calculate_tec_section(sec: section) -> float:
    ln_rk = [np.log(sec.de[i] / sec.di[i]) / sec.k_values[i] for i in range(sec.Nl)]

    Keq = np.log(sec.de[0] / sec.di[-1]) / np.sum(ln_rk)

    sec_tec = (2 * np.pi * Keq) / np.log((sec.de[0] / 2) / (sec.di[-1] / 2))

    return sec_tec


def test_section_initialization_failed() -> None:
    de = np.array([0.3490, 0.3410, 0.1956, 0.1902, 0.1896, 0.1890])
    di = np.array([0.3410, 0.1956, 0.1902, 0.1896, 0.1890, 0.1524])
    k_values = np.array([0.2250, 0.1680, 0.2250, 0.2250, 0.2940])
    Nl = 6

    with pytest.raises(ValueError) as except_info:
        section(de=de, di=di, Nl=Nl, k_values=k_values)

    assert (
        "Filled properties size don't match with layer number when checking section data"
        in str(except_info.value)
    )


@pytest.mark.parametrize(
    "de, di, k_values, tec_expected",
    [
        pytest.param(
            np.array([0.3490, 0.3410, 0.1956, 0.1902, 0.1896, 0.1890]),
            np.array([0.3410, 0.1956, 0.1902, 0.1896, 0.1890, 0.1524]),
            np.array([0.2250, 0.1680, 0.2250, 0.2250, 0.2940, 45.0]),
            1.7622207772294436,
            id="riser",
        ),
        pytest.param(
            np.array([0.3432, 0.3352, 0.2098, 0.2044, 0.2038, 0.2032]),
            np.array([0.3352, 0.2098, 0.2044, 0.2038, 0.2032, 0.1524]),
            np.array([0.2250, 0.1680, 0.2250, 0.2250, 0.2940, 45.0]),
            2.067293335192955,
            id="flowline",
        ),
        pytest.param(
            np.array([0.3175, 0.2413, 0.2159, 0.1397]),
            np.array([0.2413, 0.2159, 0.1397, 0.1143]),
            np.array([0.9, 45, 0.3, 45]),
            3.5640763064645427,
            id="well_section_1",
        ),
        pytest.param(
            np.array([0.3556, 0.3175, 0.2413, 0.2159, 0.1397]),
            np.array([0.3175, 0.2413, 0.2159, 0.1397, 0.1143]),
            np.array([45, 0.9, 45, 0.3, 45]),
            3.558992119783347,
            id="well_section_2",
        ),
        pytest.param(
            np.array([0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397]),
            np.array([0.3556, 0.3175, 0.2413, 0.2159, 0.1397, 0.1143]),
            np.array([0.9, 45, 0.58, 45, 0.3, 45]),
            3.0177953379331415,
            id="well_section_3",
        ),
        pytest.param(
            np.array([0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397]),
            np.array([0.3556, 0.3175, 0.2413, 0.2159, 0.1397, 0.1143]),
            np.array([0.58, 45, 0.58, 45, 0.3, 45]),
            2.903635114926663,
            id="well_section_4",
        ),
        pytest.param(
            np.array([0.6858, 0.508, 0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397]),
            np.array([0.508, 0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397, 0.1143]),
            np.array([0.9, 45, 0.58, 45, 0.58, 45, 0.3, 45]),
            2.5109525067994163,
            id="well_section_5",
        ),
        pytest.param(
            np.array(
                [
                    0.9144,
                    0.762,
                    0.6858,
                    0.508,
                    0.4064,
                    0.3556,
                    0.3175,
                    0.2413,
                    0.2159,
                    0.1397,
                ]
            ),
            np.array(
                [
                    0.762,
                    0.6858,
                    0.508,
                    0.4064,
                    0.3556,
                    0.3175,
                    0.2413,
                    0.2159,
                    0.1397,
                    0.1143,
                ]
            ),
            np.array([0.9, 45, 0.9, 45, 0.58, 45, 0.58, 45, 0.3, 45]),
            2.3208888318268905,
            id="well_section_6",
        ),
    ],
)
def test_tec_full_system(
    de: NDArray[np.float64],
    di: NDArray[np.float64],
    k_values: NDArray[np.float64],
    tec_expected: float,
) -> None:
    sec = section(de=de, di=di, Nl=len(de), k_values=k_values)

    tec_calc = calculate_tec_section(sec=sec)

    assert tec_calc == tec_expected
