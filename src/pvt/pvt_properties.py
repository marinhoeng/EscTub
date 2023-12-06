from attrs import define
from src.pvt.fluid_data import FluidData
from src.pvt.gas_properties import (
    calculate_Z,
    calculate_Bg,
    calculate_ρ_gas,
    calculate_Cg,
    calculate_μ_gas,
    calculate_cp_gas,
)

from src.pvt.oil_properties import (
    calculate_Pb,
    calculate_Rs,
    calculate_ρ_oil,
    calculate_μ_oil,
    calculate_cp_oil,
    calculate_Co,
    calculate_Bo,
)


@define
class PVTProperties:
    Pb: float | None = None
    Rs: float | None = None
    ρ_oil: float | None = None
    μ_oil: float | None = None
    Bo: float | None = None
    Co: float | None = None
    ρ_gas: float | None = None
    μ_gas: float | None = None
    Bg: float | None = None
    Cg: float | None = None
    Z: float | None = None
    cp_gas: float | None = None
    cp_oil: float | None = None
    σog: float | None = None


    #ρ_gas: float | None = None
    #ρ_oil: float | None = None
    #Z: float | None = None
    #Bg: float | None = None
    #Cg: float | None = None
    #μ_gas: float | None = None
    #Pb: float | None = None
    #Rs: float | None = None
    #μ_oil: float | None = None
    #Co: float | None = None
    #Bo: float | None = None
    #cp_gas: float | None = None
    #cp_oil: float | None = None
    #σog: float | None = None


@define
class PVTPropertiesMixture:
    ρ_NS: float
    μ_NS: float
    cp_NS: float
    cp_slip: float
    ρ_slip: float
    μ_slip: float


def calculate_pvt_properties(fd: FluidData, P: float, T: float) -> PVTProperties:
    Pb = calculate_Pb(fd=fd, T=T)

    if P < Pb:
        Z = calculate_Z(fd=fd, P=P, T=T)
        ρ_gas = calculate_ρ_gas(fd=fd, P=P, T=T, Z=Z)
        Bg = calculate_Bg(fd=fd, P=P, T=T, Z=Z)
        Cg = calculate_Cg(fd=fd, P=P, T=T, Z=Z)
        μ_gas = calculate_μ_gas(fd=fd, P=P, T=T, Z=Z)
        cp_gas = calculate_cp_gas(fd=fd, P=P, T=T)

    else:
        Z = 0.
        ρ_gas = 0.
        Bg = 0.
        Cg = 0.
        μ_gas = 0.
        cp_gas = 0.

    # Oil
    Rs = calculate_Rs(fd=fd, P=P, T=T, Pb=Pb)
    Bo = calculate_Bo(fd=fd, P=P, T=T, Rs=Rs, Pb=Pb)
    Co = calculate_Co(fd=fd, P=P, T=T, Pb=Pb)
    ρ_oil = calculate_ρ_oil(fd=fd, P=P, T=T, Pb=Pb, Rs=Rs)
    μ_oil = calculate_μ_oil(fd=fd, P=P, T=T, Pb=Pb)
    cp_oil = calculate_cp_oil(fd=fd, P=P, T=T)
    σog = 0.00841  # N/m

    return PVTProperties(
        Pb=Pb,
        Rs=Rs,
        ρ_oil=ρ_oil,
        μ_oil=μ_oil,
        Bo=Bo,
        Co=Co,
        ρ_gas=ρ_gas,
        μ_gas=μ_gas,
        Bg=Bg,
        Cg=Cg,
        Z=Z,
        cp_gas=cp_gas,
        cp_oil=cp_oil,
        σog=σog,
    )


def calculate_pvt_properties_mixture(PVTOG: PVTProperties, λL: float, HL: float) -> PVTPropertiesMixture:
    ρ_NS = PVTOG.ρ_oil * λL + PVTOG.ρ_gas * (1. - λL)
    μ_NS = PVTOG.μ_oil * λL + PVTOG.μ_gas * (1. - λL)
    cp_NS = PVTOG.cp_oil * λL + PVTOG.cp_gas * (1. - λL)
    cp_slip = PVTOG.cp_oil * HL + PVTOG.cp_gas * (1. - HL)
    ρ_slip = PVTOG.ρ_oil * HL + PVTOG.ρ_gas * (1. - HL)
    μ_slip = PVTOG.μ_oil * HL + PVTOG.μ_gas * (1. - HL)

    return PVTPropertiesMixture(
        ρ_NS=ρ_NS,
        μ_NS=μ_NS,
        cp_NS=cp_NS,
        cp_slip=cp_slip,
        ρ_slip=ρ_slip,
        μ_slip=μ_slip
    )
