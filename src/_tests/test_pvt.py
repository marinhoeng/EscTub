import numpy as np
import pytest
from pytest import approx
from pytest_regressions.num_regression import NumericRegressionFixture

from pvt.fluid_data import FluidData
from pvt.gas_properties import (
    calculate_reduced_properties,
    calculate_Z,
    calculate_Bg,
    calculate_ρ_gas,
    calculate_Cg,
    calculate_μ_gas,
)
from pvt.oil_properties import (
    calculate_Rs,
    calculate_Pb,
    calculate_ρ_oil,
    calculate_μ_oil,
    calculate_Bo,
    calculate_Co,
)
from pvt.pvt_properties import (
    calculate_pvt_properties,
)


def test_fluid_data_initialization() -> None:
    fd = FluidData()

    fd = fd.set_fluid_data(API=30.0, dg=0.72, RGO=125)

    assert fd.MMg == 0.0208512
    assert fd.do == approx(0.8761609907120743, rel=1e-12)


def test_gas_properties() -> None:
    P = 100e5
    T = 350

    fd = FluidData()

    fd = fd.set_fluid_data(API=30, dg=0.725, RGO=75.9)

    Ppr, Tpr = calculate_reduced_properties(fd=fd, P=P, T=T)

    assert Ppr == 2.1706904916067526
    assert Tpr == 1.5866831946166107

    Z = calculate_Z(fd=fd, P=P, T=T)
    assert Z == 0.4399209191305883

    Bg = calculate_Bg(fd=fd, P=P, T=T, Z=Z)
    assert Bg == 0.005403852187283049

    ρ_gas = calculate_ρ_gas(fd=fd, P=P, T=T, Z=Z)
    assert ρ_gas == 164.015119807712

    Cg = calculate_Cg(fd=fd, P=P, T=T, Z=Z)
    assert Cg == 01.8579585580956067e-07

    μ_gas = calculate_μ_gas(fd=fd, P=P, T=T, Z=Z)
    assert μ_gas == 1.9404687468098005e-05


@pytest.mark.parametrize(
    "P, Prop_values_expected",
    [
        (
            100e5,
            np.array(
                [
                    17647166.250601854,  # Pb
                    42.89239722650518,  # Rs
                    1.1517093539834045,  # Bo
                    9.515825692573415e-09,  # Co
                    793.4837150544658,  # ρ_oil
                    0.0013844765462768071,  # μ_oil
                ]
            ),
        ),
        (
            200e5,
            np.array(
                [
                    17647166.250601854,  # Pb
                    75.9,  # Rs
                    1.229445500157278,  # Bo
                    9.790197507449094e-10,  # Co
                    768.891263393506,  # ρ_oil
                    0.0010165067256822698,  # μ_oil
                ]
            ),
        ),
        (
            17647166.250601854,
            np.array(
                [
                    17647166.250601854,  # Pb
                    75.9,  # Rs
                    1.2322807560683378,  # Bo
                    1.0541284320063735e-09,  # Co
                    765.3571733069515,  # ρ_oil
                    0.0009841933222653654,  # μ_oil
                ]
            ),
        ),
    ],
)
def test_calc_oil_properties(P: float, Prop_values_expected: np.ndarray) -> None:
    T = 350

    fd = FluidData()
    fd = fd.set_fluid_data(API=30, dg=0.725, RGO=75.9)

    Pb = calculate_Pb(fd=fd, T=T)
    assert Pb == Prop_values_expected[0]

    Rs = calculate_Rs(fd=fd, P=P, T=T, Pb=Pb)
    assert Rs == Prop_values_expected[1]

    Bo = calculate_Bo(fd=fd, P=P, T=T, Rs=Rs, Pb=Pb)
    assert Bo == Prop_values_expected[2]

    Co = calculate_Co(fd=fd, P=P, T=T)
    assert Co == Prop_values_expected[3]

    ρ_oil = calculate_ρ_oil(fd=fd, P=P, T=T, Pb=Pb, Rs=Rs)
    assert ρ_oil == Prop_values_expected[4]

    μ_oil = calculate_μ_oil(fd=fd, P=P, T=T, Pb=Pb)
    assert μ_oil == Prop_values_expected[5]


def test_PVTProperties(num_regression: NumericRegressionFixture) -> None:
    fd = FluidData()

    fd = fd.set_fluid_data(API=30.0, dg=0.72, RGO=125)

    PVTResults = calculate_pvt_properties(fd=fd, P=100e5, T=350)

    num_regression.check(
        {
            "Pb": PVTResults.Pb,
            "ρ_gas": PVTResults.ρ_gas,
            "Z": PVTResults.Z,
            "Bg": PVTResults.Bg,
            "Cg": PVTResults.Cg,
            "μ_gas": PVTResults.μ_gas,
            "ρ_oil": PVTResults.ρ_oil,
            "Rs": PVTResults.Rs,
            "μ_oil": PVTResults.μ_oil,
            "Co": PVTResults.Co,
            "Bo": PVTResults.Bo,
            "cp_gas": PVTResults.cp_gas,
            "cp_oil": PVTResults.cp_oil,
            "σog": PVTResults.σog,
        }
    )
