
class FluidData:

    def __init__(self):
        self.API = 0.
        self.do = 0.
        self.dg = 0.
        self.MMg = 0.
        self.RGO = 0.
        self.Ppc = 0.
        self.Tpc = 0.

    def set_fluid_data(self, API: float, dg: float, RGO: float):

        MMg = 28.96 * dg / 1000  # [kg/mol]

        do = 141.5 / (API + 131.5)

        Ppc, Tpc = calculate_critical_properties(dg=dg)

        self.dg = dg
        self.API = API
        self.do = do
        self.RGO = RGO
        self.MMg = MMg
        self.Ppc = Ppc
        self.Tpc = Tpc

        return self


def calculate_critical_properties(dg: float) -> tuple[float, float]:

    if dg < 0.75:
        Ppc = (677 + 15 * dg - 37.5 * dg ** 2)  # psia
        Tpc = (168 + 325 * dg - 12.5 * dg ** 2)  # °R

    else:
        Ppc = (706 - 51.7 * dg - 11.1 * dg ** 2)
        Tpc = (187 + 330 * dg - 71.5 * dg ** 2)

    # Ppc = Converter.CalcPressure(Ppc, 'psia', 'pa')[0]
    # Tpc = Converter.CalcTemperature(Tpc, 'R', 'K')[0]

    return Ppc, Tpc



