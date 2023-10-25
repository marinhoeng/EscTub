from gas_properties import calculate_reduced_properties
from fluid_data import FluidData
import pytest
from pytest import approx


def test_fluid_data_initialization() -> None:

    fd = FluidData()

    fd = fd.set_fluid_data(API=30.0, dg=0.72, RGO=125)

    assert fd.MMg == 0.0208512
    assert fd.do == approx(0.8761609907120743, rel=1e-12)


def test_calc_ppr_tpr() -> None:
    P = 100e5
    T = 350

    fd = FluidData()

    fd.Ppc = 61e5
    fd.Tpc = 303

    Ppr, Tpr = calculate_reduced_properties(fd=fd, P=P, T=T)

    ref_Ppr = 1.639344262295082
    ref_Tpr = 1.155115511551155

    print("Ppr = ", Ppr, "Tpr =", Tpr)

    assert Ppr == ref_Ppr
    assert Tpr == ref_Tpr
