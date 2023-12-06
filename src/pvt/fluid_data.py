from src.TTPUnitConvert import TTPUnitConvert

Unit: TTPUnitConvert = TTPUnitConvert()


class FluidData:
    def __init__(self):
        self.API: float = 0.0
        self.do: float = 0.0
        self.dg: float = 0.0
        self.MMg: float = 0.0
        self.RGO: float = 0.0
        self.Ppc: float = 0.0
        self.Tpc: float = 0.0
        self.Psc: float = 101325.0  # Pa
        self.Tsc: float = 288.706  # K
        self.R: float = 8.314  # Pa*m3/mol*K

    def set_fluid_data(self, API: float, dg: float, RGO: float):
        MMg = 28.96 * dg / 1000  # [kg/kg-mol]

        do = 141.5 / (API + 131.5)

        Ppc, Tpc = calculate_critical_properties(dg=dg)

        self.dg: float = dg
        self.API: float = API
        self.do: float = do
        self.RGO: float = RGO
        self.MMg: float = MMg
        self.Ppc: float = Ppc
        self.Tpc: float = Tpc

        return self


def calculate_critical_properties(dg: float) -> tuple[float, float]:
    if dg < 0.75:
        Ppc = 677 + 15 * dg - 37.5 * dg**2  # psia
        Tpc = 168 + 325 * dg - 12.5 * dg**2  # °R

    else:
        Ppc = 706 - 51.7 * dg - 11.1 * dg**2  # psia
        Tpc = 187 + 330 * dg - 71.5 * dg**2  # °R

    Ppc = Unit.mCalc_Conv_Pressure(Ppc, "psi", "pa")
    Tpc = Unit.mCalc_Conv_Temperature(Tpc, "R", "K")

    return Ppc, Tpc
