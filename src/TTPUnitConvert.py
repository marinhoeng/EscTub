class TTPUnitConvert:

    def __init__(self):
        
        # Pressure Convertion Dictionary
        self.__fPressure = {'pa': 1.0, 'kpa': 1.e-3, 'mpa': 1.e-6, 'atm': 9.86923266716013e-6, 'bar': 1.e-5, 'psi': 1.45037737730209e-4, 'torr': 0.007500617, 'mmhg': 0.007500617}

        # Volume Convertion Dictionary
        self.__fVolume = {'m3': 1.0, 'cm3': 1.0e6, 'l': 1.0e3, 'bbl': 6.289814, 'gal': 264.172053, 'in3': 61023.744242, 'ft3': 35.314667, 'yd3': 1.307951}

        # Density Convertion Dictionary
        self.__fDensity = {'kg/m3': 1.0, 'kg/l': 0.001, 'g/cm3': 0.001, 'g/l': 1.0, 'g/ml': 0.001, 'lb/l': 0.00220462, 'lb/in3': 0.000036125, 'lb/ft3': 0.062424, 'ppb': 1.0e6, 'percent': 0.1, 'ppm': 1.0e3, 'mg/l': 1.0e3, 'kg/cm3': 1.0e-6, 'g/m3': 1.0e3}

        # Viscosity Conversion Dictionary
        self.__fViscosity = {'pa·s': 1.0, 'p': 10.0, 'cp': 1.0e3, 'microp': 1.0e7, 'dyne·s/cm2': 10.0, 'g/(cm·s)': 10.0}

        # Mass Conversion Dictionary
        self.__fMass = {'kg': 1.0, 'g': 1.0e3, 'mg': 1.0e6, 'lb': 2.204623, 'oz': 35.273968, 't': 0.001}

        # Volume Ratio Convertion Dictionary
        self.__fVolration = {'m3/m3': 1.0, 'scf/stb': 5.61458333333333, 'mscf/stb': 5.61458333333333e-3, 'stb/scf': 0.178107606679035, 'stb/mscf': 178.107606679035, 'bbl/stb': 1.0}

        # Length Convertion Dictionary
        self.__fLength = {'m': 1.0, 'km': 0.001, 'cm': 1.0e2, 'mm': 1.0e3, 'in': 39.3701, 'yd': 1.093613, 'ft': 3.280839}

        # Compressibility Convertion Dictionary
        self.__fComp = {'pa-1': 1.0, 'psi-1': 6894.75729316836, 'bar-1': 1.0e5, 'atm-1': 101325, 'kpa-1': 1.e3, 'mpa-1': 1.e6, 'torr-1': 133.3224, 'mmhg-1': 133.3224}

        # Surface Tension Convertion Dictionary
        self.__fSurfaceTension = {'n/m': 1.0, 'mn/m': 1.0e3, 'gf/cm': 1.019716213, 'dyn/cm': 1.0e3, 'pdl/in': 0.18371855, 'lbf/in': 0.005710147, 'erg/cm2': 1.0e3}

        # Velocity Convertion Dictionary
        self.__fVelocity = {'m/s': 1.0, 'km/h': 3.6, 'km/s': 1.0e-3, 'mi/h': 2.237, 'ft/s': 3.281}

        # Energy Convertion Dictionary
        self.__fEnergy = {'j': 1.0, 'kg·f·m': 0.10197160000000001, 'erg': 1.e7, 'w·s': 1.0, 'kw·h': 2.777778e-7, 'cal': 0.238846, 'ft·lb·f': 0.7375621, 'btu': 9.47817e-4, 'thm': 9.47817e-9, 'n·m': 1.0}

        # Mass Flow Convertion Dictionary
        self.__fMassFlow = {'kg/s': 1.0, 'g/d': 8.64e7, 'g/h': 3.6e6, 'g/min': 6.0e4, 'g/s': 1000.0, 'kg/d': 8.64e4, 'kg/h': 3.6e3, 'kg/min': 60.0, 'lb/d': 190479.5499039, 'lb/h': 7936.6479127, 'lb/min': 132.2774652, 'lb/s': 2.2046244, 'ton/d': 86.4, 'ton/h': 3.6, 'ton/min': 6.0e-2}

        # Volumetric Flow Convertion Dictionary
        self.__fVolFlow = {'m3/s': 1.0}

        # Productivity Index Convertion Dictionary
        self.__fIP = {'m3/(pa·s)': 1.0, 'm3/(kpa·d)': 86400000.0, 'bbl/(psi·d)': 3746884494.132201}

        # Molar Flow Convertion Dictionary
        self.__fMolarFlow = {'mol/s': 1.0, 'emol/s': 1.0e-18, 'petamol/s': 1.0e-15, 'tmol/s': 1.0e-12, 'gmol/s': 1.0e-9, 'megamol/s': 1.0e-6, 'kmol/s': 1.0e-3, 'hmol/s': 1.0e-2, 'dmol/s': 10.0, 'cmol/s': 100.0, 'mmol/s': 1.0e3, 'micromol/s': 1.0e6, 'nmol/s': 1.0e9, 'mol/min': 60.0,'mol/h': 3600.0, 'mol/d': 86400.0, 'mmol/min': 6.0e4, 'mmol/h': 3.6e6, 'mmol/d': 8.64e7, 'kmol/min': 6.0e-2, 'kmol/h': 3.6, 'kmol/d': 86.4}

        # Work Convertion Dictionary
        self.__fWork = {'j': 1.0, 'n/m': 1.0, 'kw/h': 2.7778e-7, 'ft/lb': 0.737562, 'hp·h': 3.725061359980878e-7, 'erg': 1.0e7, 'btu': 9.47817e-4}

        # Molar Volume Convertion Dictionary
        self.__fMolarVolume = {'m3/mol': 1.0, 'cm3/mol': 1.0e6, 'dm3/mol': 1.0e3, 'ml/mol': 1.0e6, 'l/mol': 1.0e3}

        # Specific Energy Convertion Dictionary
        self.__fSpecificEnergy = {'j/kg': 1.0, 'j/g': 1.0e3, 'cal/g':  2.388459e-4, 'btu/lb':  4.299226e-4}

        # Molar Density Convertion Dictionary
        self.__fMolarDensity = {'mol/m3': 1.0, 'mmol/m3': 1.0e3, 'micromol/m3': 1.0e6, 'mol/l': 1.0e-3, 'micromol/l': 1.0e3, 'mmol/l': 1.0}

        # Permeability Convertion Dictionary
        self.__fPermeability = {'m2': 1.0, 'sq·ft': 10.764262648008613, 'darcy': 1013249965828.1448}

        # Thermal Conductivity Convertion Dictionary
        self.__fThermalConductivity = {'w/(m·k)': 1.0, 'kw/(m·k)': 1.e-3, 'cal/(s·cm·c)': 0.00238846, 'btu/(h·ft·f)': 0.5777893, 'cal/(s·m·c)': 0.23884599999999997}

        # Heat Capacity
        self.__fHeatCapacity = {'j/k': 1.0, 'j/c': 1.0, 'cal/c': 0.2388459, 'btu/f': 5.265649e-4}

        # Angle
        self.__fAngle = {'radian': 1.0, 'degree': 57.295779513082, 'minutes': 3437.7467707849, 'seconds': 206264.8062471, 'revolution': 0.1591549430919}


        #--- Create List of Units from Dictionary ---#
        self.__fListPressure = list(self.__fPressure)
        self.__fListVolume = list(self.__fVolume)
        self.__fListDensity = list(self.__fDensity)
        self.__fListViscosity = list(self.__fViscosity)
        self.__fListMass = list(self.__fMass)
        self.__fListVolration = list(self.__fVolration)
        self.__fListLength = list(self.__fLength)
        self.__fListComp = list(self.__fComp)
        self.__fListSurfaceTension = list(self.__fSurfaceTension)
        self.__fListVelocity = list(self.__fVelocity)
        self.__fListEnergy = list(self.__fEnergy)
        self.__fListMassFlow = list(self.__fMassFlow)
        self.__fListIP = list(self.__fIP)
        self.__fListMolarFlow = list(self.__fMolarFlow)
        self.__fListVolFlow = list(self.__fVolFlow)
        self.__fListWork = list(self.__fWork)
        self.__fListMolarVolume = list(self.__fMolarVolume)
        self.__fListSpecificEnergy = list(self.__fSpecificEnergy)
        self.__fListMolarDensity = list(self.__fMolarDensity)
        self.__fListPermeability = list(self.__fPermeability)
        self.__fListThermalConductivity = list(self.__fThermalConductivity)
        self.__fListHeatCapacity = list(self.__fHeatCapacity)
        self.__fListAngle = list(self.__fAngle)
        self.__fListTemperature = ['k', 'c', 'f','r']
        self.__fListJouleTC = ['k/bar', 'k/pa', 'k/kpa', 'k/mpa', 'k/atm', 'k/psi', 'k/torr','k/mmhg','c/pa','c/kpa','c/mpa','c/atm','c/bar','c/psi','c/torr','c/mmhg','f/pa','f/kpa','f/mpa','f/atm','f/bar','f/psi','f/torr','f/mmHg','r/pa','r/kpa','r/mpa','r/atm','r/bar','r/psi','r/torr','r/mmHg']



    #--- Calculation Methods for Units Conversion ---#

    # Temperature:
    def mCalc_Conv_Temperature(self, t_in, unit_in, unit_out):

        unit_in = unit_in.upper()
        unit_out = unit_out.upper()

        tsi = self.sCalc_Conv_ISTemperature(t_in, unit_in)
        rTemperature = self.sCalc_Conv_Temperature(tsi, unit_out)

        return rTemperature

    # Velocity:
    def mCalc_Conv_Velocity(self, vel_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fVelocity.get(unit_in)
        cv_out = self.__fVelocity.get(unit_out)

        velsi = self.sCalc_Conv_IS(vel_in, cv_in)
        rVelocity = self.sCalc_Conv_Unit(velsi, cv_out)

        return rVelocity

    # Angle:
    def mCalc_Conv_Angle(self, ang_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fAngle.get(unit_in)
        cv_out = self.__fAngle.get(unit_out)

        angsi = self.sCalc_Conv_IS(ang_in, cv_in)
        rAngle = self.sCalc_Conv_Unit(angsi, cv_out)

        return rAngle

    # Energy:
    def mCalc_Conv_Energy(self, en_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fEnergy.get(unit_in)
        cv_out = self.__fEnergy.get(unit_out)

        ensi = self.sCalc_Conv_IS(en_in, cv_in)
        rEnergy = self.sCalc_Conv_Unit(ensi, cv_out)

        return rEnergy

    # Mass Flow:
    def mCalc_Conv_MassFlow(self, mf_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fMassFlow.get(unit_in)
        cv_out = self.__fMassFlow.get(unit_out)

        mfsi = self.sCalc_Conv_IS(mf_in, cv_in)
        rMassFlow = self.sCalc_Conv_Unit(mfsi, cv_out)

        return rMassFlow

    # Production Index:
    def mCalc_Conv_IP(self, prodin_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fIP.get(unit_in)
        cv_out = self.__fIP.get(unit_out)

        prodinsi = self.sCalc_Conv_IS(prodin_in, cv_in)
        rIP = self.sCalc_Conv_Unit(prodinsi, cv_out)

        return rIP

    # Molar Flow:
    def mCalc_Conv_MolarFlow(self, molf_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fMolarFlow.get(unit_in)
        cv_out = self.__fMolarFlow.get(unit_out)

        molfsi = self.sCalc_Conv_IS(molf_in, cv_in)
        rMolarFlow = self.sCalc_Conv_Unit(molfsi, cv_out)

        return rMolarFlow

    # Work:
    def mCalc_Conv_Work(self, work_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fWork.get(unit_in)
        cv_out = self.__fWork.get(unit_out)

        worksi = self.sCalc_Conv_IS(work_in, cv_in)
        rWork = self.sCalc_Conv_Unit(worksi, cv_out)

        return rWork

    # Molar Volume:
    def mCalc_Conv_MolarVolume(self, molvol_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fMolarVolume.get(unit_in)
        cv_out = self.__fMolarVolume.get(unit_out)

        molvolsi = self.sCalc_Conv_IS(molvol_in, cv_in)
        rMolarVolume = self.sCalc_Conv_Unit(molvolsi, cv_out)

        return rMolarVolume

    # Specific Energy:
    def mCalc_Conv_SpecificEnergy(self, spen_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fSpecificEnergy.get(unit_in)
        cv_out = self.__fSpecificEnergy.get(unit_out)

        spensi = self.sCalc_Conv_IS(spen_in, cv_in)
        rSpecificEnergy = self.sCalc_Conv_Unit(spensi, cv_out)

        return rSpecificEnergy

    # Molar Density:
    def mCalc_Conv_MolarDensity(self, molden_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fMolarDensity.get(unit_in)
        cv_out = self.__fMolarDensity.get(unit_out)

        moldensi = self.sCalc_Conv_IS(molden_in, cv_in)
        rMolarDensity = self.sCalc_Conv_Unit(moldensi, cv_out)

        return rMolarDensity

    # Permeability:
    def mCalc_Conv_Permeability(self, permeab_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fPermeability.get(unit_in)
        cv_out = self.__fPermeability.get(unit_out)

        permeabsi = self.sCalc_Conv_IS(permeab_in, cv_in)
        rPermeability = self.sCalc_Conv_Unit(permeabsi, cv_out)

        return rPermeability

    # Thermal Conductivity:
    def mCalc_Conv_ThermalConductivity(self, thermcon_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fThermalConductivity.get(unit_in)
        cv_out = self.__fThermalConductivity.get(unit_out)

        thermconsi = self.sCalc_Conv_IS(thermcon_in, cv_in)
        rThermalConductivity = self.sCalc_Conv_Unit(thermconsi, cv_out)

        return rThermalConductivity

    # Heat Capacity:
    def mCalc_Conv_HeatCapacity(self, heatcap_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fHeatCapacity.get(unit_in)
        cv_out = self.__fHeatCapacity.get(unit_out)

        heatcapsi = self.sCalc_Conv_IS(heatcap_in, cv_in)
        rHeatCapacity = self.sCalc_Conv_Unit(heatcapsi, cv_out)

        return rHeatCapacity

    # Pressure:
    def mCalc_Conv_Pressure(self, p_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fPressure.get(unit_in)
        cv_out = self.__fPressure.get(unit_out)

        psi = self.sCalc_Conv_IS(p_in, cv_in)
        rPressure = self.sCalc_Conv_Unit(psi, cv_out)

        return rPressure

    # Volume:
    def mCalc_Conv_Volume(self, v_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fVolume.get(unit_in)
        cv_out = self.__fVolume.get(unit_out)

        vsi = self.sCalc_Conv_IS(v_in, cv_in)
        rVolume = self.sCalc_Conv_Unit(vsi, cv_out)

        return rVolume

    # Density:
    def mCalc_Conv_Density(self, rho_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fDensity.get(unit_in)
        cv_out = self.__fDensity.get(unit_out)

        rho_si = self.sCalc_Conv_IS(rho_in, cv_in)
        rDensity = self.sCalc_Conv_Unit(rho_si, cv_out)

        return rDensity

    # Viscosity:
    def mCalc_Conv_Viscosity(self, visc_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fViscosity.get(unit_in)
        cv_out = self.__fViscosity.get(unit_out)

        visc_si = self.sCalc_Conv_IS(visc_in, cv_in)
        rViscosity = self.sCalc_Conv_Unit(visc_si, cv_out)

        return rViscosity

    # Mass:
    def mCalc_Conv_Mass(self, mass_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fMass.get(unit_in)
        cv_out = self.__fMass.get(unit_out)

        mass_si = self.sCalc_Conv_IS(mass_in, cv_in)
        rMass = self.sCalc_Conv_Unit(mass_si, cv_out)

        return rMass

    # Volume Ration:
    def mCalc_Conv_Volration(self, volration_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fVolration.get(unit_in)
        cv_out = self.__fVolration.get(unit_out)

        volration_si = self.sCalc_Conv_IS(volration_in, cv_in)
        rVolration = self.sCalc_Conv_Unit(volration_si, cv_out)

        return rVolration

    # Length:
    def mCalc_Conv_Length(self, length_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fLength.get(unit_in)
        cv_out = self.__fLength.get(unit_out)

        length_si = self.sCalc_Conv_IS(length_in, cv_in)
        rLength = self.sCalc_Conv_Unit(length_si, cv_out)

        return rLength

    # Compressibility:
    def mCalc_Conv_Comp(self, comp_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fComp.get(unit_in)
        cv_out = self.__fComp.get(unit_out)

        comp_si = self.sCalc_Conv_IS(comp_in, cv_in)
        rComp = self.sCalc_Conv_Unit(comp_si, cv_out)

        return rComp

    # Surface Tension:
    def mCalc_Conv_SurfaceTension(self, st_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        cv_in = self.__fSurfaceTension.get(unit_in)
        cv_out = self.__fSurfaceTension.get(unit_out)

        st_si = self.sCalc_Conv_IS(st_in, cv_in)
        rSurfaceTension = self.sCalc_Conv_Unit(st_si, cv_out)

        return rSurfaceTension



    # --- GENERAL METHOD FOR CONVERSION UNITS (AS DOUBLE, AS VECTOR AND AS MATRIX) --- #

    def mCalc_Conv_Double(self,inputUnit, outputUnit, input):

        # inputUnit = Unit that we have 
        # outputUnit = Unit that we wanna know
        # input = Input as Double of what we wanna convert with pressure, temperature values (for exemple)

        # Passing the input datas to lower case

        inputUnit = inputUnit.lower()
        outputUnit = outputUnit.lower()

        outputDouble = 777.0 # Inicial Value as Double

        if inputUnit in self.__fListPressure and outputUnit in self.__fListPressure:
          outputDouble = self.mCalc_Conv_Pressure(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListVolume and outputUnit in self.__fListVolume:
          outputDouble = self.mCalc_Conv_Volume(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListDensity and outputUnit in self.__fListDensity:
          outputDouble = self.mCalc_Conv_Density(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListViscosity and outputUnit in self.__fListViscosity:
         outputDouble = self.mCalc_Conv_Viscosity(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListMass and outputUnit in self.__fListMass:
         outputDouble = self.mCalc_Conv_Mass(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListVolration and outputUnit in self.__fListVolration:
          outputDouble = self.mCalc_Conv_Volration(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListLength and outputUnit in self.__fListLength:
         outputDouble = self.mCalc_Conv_Length(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListComp and outputUnit in self.__fListComp:
         outputDouble = self.mCalc_Conv_Comp(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListSurfaceTension and outputUnit in self.__fListSurfaceTension:
         outputDouble = self.mCalc_Conv_SurfaceTension(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListTemperature and outputUnit in self.__fListTemperature:
         outputDouble = self.mCalc_Conv_Temperature(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListVelocity and outputUnit in self.__fListVelocity:
         outputDouble = self.mCalc_Conv_Velocity(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListThermalConductivity and outputUnit in self.__fListThermalConductivity:
         outputDouble = self.mCalc_Conv_ThermalConductivity(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListHeatCapacity and outputUnit in self.__fListHeatCapacity:
         outputDouble = self.mCalc_Conv_HeatCapacity(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListEnergy and outputUnit in self.__fListEnergy:
         outputDouble = self.mCalc_Conv_Energy(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListMassFlow and outputUnit in self.__fListMassFlow:
         outputDouble = self.mCalc_Conv_MassFlow(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListIP and outputUnit in self.__fListIP:
         outputDouble = self.mCalc_Conv_IP(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListMolarFlow and outputUnit in self.__fListMolarFlow:
         outputDouble = self.mCalc_Conv_MolarFlow(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListWork and outputUnit in self.__fListWork:
         outputDouble = self.mCalc_Conv_Work(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListMolarVolume and outputUnit in self.__fListMolarVolume:
         outputDouble = self.mCalc_Conv_MolarVolume(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListSpecificEnergy and outputUnit in self.__fListSpecificEnergy:
         outputDouble = self.mCalc_Conv_SpecificEnergy(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListMolarDensity and outputUnit in self.__fListMolarDensity:
         outputDouble = self.mCalc_Conv_MolarDensity(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListPermeability and outputUnit in self.__fListPermeability:
         outputDouble = self.mCalc_Conv_Permeability(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListJouleTC and outputUnit in self.__fListJouleTC:
         outputDouble = self.mCalc_Conv_JouleTC(input, inputUnit, outputUnit)

        elif inputUnit in self.__fListAngle and outputUnit in self.__fListAngle:
         outputDouble = self.mCalc_Conv_Angle(input, inputUnit, outputUnit)

        else:
         print(' Something goes wrong! :( ')

        rOutputDouble = outputDouble

        return rOutputDouble



    def mCalc_Conv_Vector(self, inputUnit, outputUnit, input):

      # inputUnit = Unit that we have 
      # outputUnit = Unit that we wanna know
      # input = Input Vector of what we wanna convert with pressure, temperature values (for exemple)

      # Passing the input datas to lower case

        inputUnit = inputUnit.lower()
        outputUnit = outputUnit.lower()

        outputVector = []

        for i in range(0, len(input)):
              
          if inputUnit in self.__fListPressure and outputUnit in self.__fListPressure :
             outputVector.append(self.mCalc_Conv_Pressure(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListVolume and outputUnit in self.__fListVolume :
             outputVector.append(self.mCalc_Conv_Volume(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListDensity and outputUnit in self.__fListDensity :
             outputVector.append(self.mCalc_Conv_Density(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListViscosity and outputUnit in self.__fListViscosity :
             outputVector.append(self.mCalc_Conv_Viscosity(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListMass and outputUnit in self.__fListMass :
             outputVector.append(self.mCalc_Conv_Mass(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListVolration and outputUnit in self.__fListVolration :
             outputVector.append(self.mCalc_Conv_Volration(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListLength and outputUnit in self.__fListLength :
             outputVector.append(self.mCalc_Conv_Length(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListComp and outputUnit in self.__fListComp :
             outputVector.append(self.mCalc_Conv_Comp(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListSurfaceTension and outputUnit in self.__fListSurfaceTension :
             outputVector.append(self.mCalc_Conv_SurfaceTension(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListTemperature and outputUnit in self.__fListTemperature :
             outputVector.append(self.mCalc_Conv_Temperature(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListVelocity and outputUnit in self.__fListVelocity :
             outputVector.append(self.mCalc_Conv_Velocity(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListThermalConductivity and outputUnit in self.__fListThermalConductivity :
             outputVector.append(self.mCalc_Conv_ThermalConductivity(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListHeatCapacity and outputUnit in self.__fListHeatCapacity :
             outputVector.append(self.mCalc_Conv_HeatCapacity(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListEnergy and outputUnit in self.__fListEnergy :
             outputVector.append(self.mCalc_Conv_Energy(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListMassFlow and outputUnit in self.__fListMassFlow :
             outputVector.append(self.mCalc_Conv_MassFlow(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListIP and outputUnit in self.__fListIP :
             outputVector.append(self.mCalc_Conv_IP(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListMolarFlow and outputUnit in self.__fListMolarFlow :
             outputVector.append(self.mCalc_Conv_MolarFlow(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListWork and outputUnit in self.__fListWork :
             outputVector.append(self.mCalc_Conv_Work(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListMolarVolume and outputUnit in self.__fListMolarVolume :
             outputVector.append(self.mCalc_Conv_MolarVolume(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListSpecificEnergy and outputUnit in self.__fListSpecificEnergy :
             outputVector.append(self.mCalc_Conv_SpecificEnergy(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListMolarDensity and outputUnit in self.__fListMolarDensity :
             outputVector.append(self.mCalc_Conv_MolarDensity(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListPermeability and outputUnit in self.__fListPermeability :
             outputVector.append(self.mCalc_Conv_Permeability(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListJouleTC and outputUnit in self.__fListJouleTC :
             outputVector.append(self.mCalc_Conv_JouleTC(input[i], inputUnit, outputUnit))
          elif inputUnit in self.__fListAngle and outputUnit in self.__fListAngle :
             outputVector.append(self.mCalc_Conv_Angle(input[i], inputUnit, outputUnit))

          else:
             print(' Something goes wrong! :( ')

        rOutputVector = outputVector  

        return rOutputVector

    
    def mCalc_Conv_Matrix(self, inputUnit, outputUnit, input):

      # inputUnit = Unit that we have 
      # outputUnit = Unit that we wanna know
      # input = Input Matrix of what we wanna convert with pressure, temperature values (for exemple)

      # Passing the input datas to lower case

      inputUnit = inputUnit.lower()
      outputUnit = outputUnit.lower()
  
  
      outputMatrix = []
    
      tempList = []



      for i in range(0, len(input)):

         for j in range(0, len(input[0])):

             if inputUnit in self.__fListPressure and outputUnit in self.__fListPressure :
               tempList.append(self.mCalc_Conv_Pressure(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListVolume and outputUnit in self.__fListVolume :
               tempList.append(self.mCalc_Conv_Volume(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListDensity and outputUnit in self.__fListDensity :
               tempList.append(self.mCalc_Conv_Density(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListViscosity and outputUnit in self.__fListViscosity :
               tempList.append(self.mCalc_Conv_Viscosity(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListMass and outputUnit in self.__fListMass :
               tempList.append(self.mCalc_Conv_Mass(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListVolration and outputUnit in self.__fListVolration :
               tempList.append(self.mCalc_Conv_Volration(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListLength and outputUnit in self.__fListLength :
               tempList.append(self.mCalc_Conv_Length(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListComp and outputUnit in self.__fListComp :
               tempList.append(self.mCalc_Conv_Comp(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListSurfaceTension and outputUnit in self.__fListSurfaceTension :
               tempList.append(self.mCalc_Conv_SurfaceTension(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListTemperature and outputUnit in self.__fListTemperature :
               tempList.append(self.mCalc_Conv_Temperature(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListVelocity and outputUnit in self.__fListVelocity :
               tempList.append(self.mCalc_Conv_Velocity(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListThermalConductivity and outputUnit in self.__fListThermalConductivity :
               tempList.append(self.mCalc_Conv_ThermalConductivity(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListHeatCapacity and outputUnit in self.__fListHeatCapacity :
               tempList.append(self.mCalc_Conv_HeatCapacity(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListEnergy and outputUnit in self.__fListEnergy :
               tempList.append(self.mCalc_Conv_Energy(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListMassFlow and outputUnit in self.__fListMassFlow :
               tempList.append(self.mCalc_Conv_MassFlow(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListIP and outputUnit in self.__fListIP :
               tempList.append(self.mCalc_Conv_IP(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListMolarFlow and outputUnit in self.__fListMolarFlow :
               tempList.append(self.mCalc_Conv_MolarFlow(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListWork and outputUnit in self.__fListWork :
               tempList.append(self.mCalc_Conv_Work(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListMolarVolume and outputUnit in self.__fListMolarVolume :
               tempList.append(self.mCalc_Conv_MolarVolume(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListSpecificEnergy and outputUnit in self.__fListSpecificEnergy :
               tempList.append(self.mCalc_Conv_SpecificEnergy(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListMolarDensity and outputUnit in self.__fListMolarDensity :
               tempList.append(self.mCalc_Conv_MolarDensity(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListPermeability and outputUnit in self.__fListPermeability :
               tempList.append(self.mCalc_Conv_Permeability(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListJouleTC and outputUnit in self.__fListJouleTC :
              tempList.append(self.mCalc_Conv_JouleTC(input[i][j], inputUnit, outputUnit))
             elif inputUnit in self.__fListAngle and outputUnit in self.__fListAngle :
              tempList.append(self.mCalc_Conv_Angle(input[i][j], inputUnit, outputUnit))


             else:
              print(' Something goes wrong! :( ')


         outputMatrix.append(tempList)
         tempList = []

  
      rOutputMatrix = outputMatrix

      return rOutputMatrix



    # --- STATIC METHODS FOR NON-LINEAR CONVERSION EQUATIONS --- #

    @staticmethod
    def sCalc_Conv_IS(x_in, cv_in):
        x_si = (1./cv_in) * x_in
        return x_si

    @staticmethod
    def sCalc_Conv_Unit(cv_out, x_si):
        x_out = cv_out * x_si
        return x_out

    @staticmethod
    def sCalc_Conv_ISTemperature(t_in, unit_in):
        if unit_in == 'K':
            rSITemperature = t_in
        elif unit_in == 'C':
            rSITemperature = t_in + 273.15
        elif unit_in == 'F':
            rSITemperature = (t_in + 459.67)/1.8
        elif unit_in == 'R':
            rSITemperature = t_in / 1.8
        else:
            print('Error: No temperature unit selected.')

        return rSITemperature

    @staticmethod
    def sCalc_Conv_Temperature(tsi, unit_out):

        if unit_out == 'K':
            rTemperatureOut = tsi
        elif unit_out == 'C':
            rTemperatureOut = tsi - 273.15
        elif unit_out == 'F':
            rTemperatureOut = 1.8 * tsi - 459.67
        elif unit_out == 'R':
            rTemperatureOut = 1.8 * tsi
        else:
            print('Error: No temperature unit selected.')

        return rTemperatureOut

    # Joule Thomson Coefficient
    def mCalc_Conv_JouleTC(self, jouthc_in, unit_in, unit_out):

        unit_in = unit_in.lower()
        unit_out = unit_out.lower()

        jouthc = self.sCalc_Conv_JouleTCIS(jouthc_in, unit_in)
        rJouleTCOut = self.sCalc_Conv_JouleTC(jouthc, unit_out)

        return rJouleTCOut

    @staticmethod
    def sCalc_Conv_JouleTCIS(jouthc_in, unit_in):

        if unit_in == 'k/pa':
            rJouleTCIS = jouthc_in
        elif unit_in == 'k/kpa':
            rJouleTCIS = jouthc_in * 1.e-3
        elif unit_in == 'k/mpa':
            rJouleTCIS = jouthc_in * 1.e-6
        elif unit_in == 'k/atm':
            rJouleTCIS = jouthc_in * 9.86923266716013e-6
        elif unit_in == 'k/bar':
            rJouleTCIS = jouthc_in * 1.e-5
        elif unit_in == 'k/psi':
            rJouleTCIS = jouthc_in * 1.45037737730209e-4
        elif unit_in == 'k/torr':
            rJouleTCIS = jouthc_in * 0.007500617
        elif unit_in == 'k/mmhg':
            rJouleTCIS = jouthc_in * 0.007500617
        elif unit_in == 'c/pa':
            rJouleTCIS = jouthc_in + 273.15
        elif unit_in == 'c/kpa':
            rJouleTCIS = (jouthc_in + 273.15) * 1.e-3
        elif unit_in == 'c/mpa':
            rJouleTCIS = (jouthc_in + 273.15) * 1.e-6
        elif unit_in == 'c/atm':
            rJouleTCIS = (jouthc_in + 273.15) * 9.86923266716013e-6
        elif unit_in == 'c/bar':
            rJouleTCIS = (jouthc_in + 273.15) * 1.e-5
        elif unit_in == 'c/psi':
            rJouleTCIS = (jouthc_in + 273.15) * 1.45037737730209e-4
        elif unit_in == 'c/torr':
            rJouleTCIS = (jouthc_in + 273.15) * 0.007500617
        elif unit_in == 'c/mmhg':
            rJouleTCIS = (jouthc_in + 273.15) * 0.007500617
        elif unit_in == 'f/pa':
            rJouleTCIS = (jouthc_in + 459.67) / 1.8
        elif unit_in == 'f/kpa':
            rJouleTCIS = (1.e-3 * jouthc_in + 459.67) / 1.8
        elif unit_in == 'f/mpa':
            rJouleTCIS = (1.e-6 * jouthc_in + 459.67) / 1.8
        elif unit_in == 'f/atm':
            rJouleTCIS = (9.86923266716013e-6 * jouthc_in + 459.67) / 1.8
        elif unit_in == 'f/bar':
            rJouleTCIS = (1.e-5 * jouthc_in + 459.67) / 1.8
        elif unit_in == 'f/psi':
            rJouleTCIS = (1.45037737730209e-4 * jouthc_in + 459.67) / 1.8
        elif unit_in == 'f/torr':
            rJouleTCIS = (0.007500617 * jouthc_in + 459.67) / 1.8
        elif unit_in == 'f/mmHg':
            rJouleTCIS = (0.007500617 * jouthc_in + 459.67) / 1.8
        elif unit_in == 'r/pa':
            rJouleTCIS = jouthc_in / 1.8
        elif unit_in == 'r/kpa':
            rJouleTCIS = (1.e-3 * jouthc_in) / 1.8
        elif unit_in == 'r/mpa':
            rJouleTCIS = (1.e-6 * jouthc_in) / 1.8
        elif unit_in == 'r/atm':
            rJouleTCIS = (9.86923266716013e-6 * jouthc_in) / 1.8
        elif unit_in == 'r/bar':
            rJouleTCIS = (1.e-5 * jouthc_in) / 1.8
        elif unit_in == 'r/psi':
            rJouleTCIS = (1.45037737730209e-4 * jouthc_in) / 1.8
        elif unit_in == 'r/torr':
            rJouleTCIS = (0.007500617 * jouthc_in) / 1.8
        elif unit_in == 'r/mmHg':
            rJouleTCIS = (0.007500617 * jouthc_in) / 1.8
        else:
            print('Error: No Joule Thomson Coefficient unit selected.')

        return rJouleTCIS

    @staticmethod
    def sCalc_Conv_JouleTC(jouthcsi, unit_out):

        if unit_out == 'k/pa':
            rJouleTCOut = jouthcsi
        elif unit_out == 'k/kpa':
            rJouleTCOut = jouthcsi / 1.e-3
        elif unit_out == 'k/mpa':
            rJouleTCOut = jouthcsi / 1.e-6
        elif unit_out == 'k/atm':
            rJouleTCOut = jouthcsi / 9.86923266716013e-6
        elif unit_out == 'k/bar':
            rJouleTCOut = jouthcsi / 1.e-5
        elif unit_out == 'k/psi':
            rJouleTCOut = jouthcsi / 1.45037737730209e-4
        elif unit_out == 'k/torr':
            rJouleTCOut = jouthcsi / 0.007500617
        elif unit_out == 'k/mmhg':
            rJouleTCOut = jouthcsi / 0.007500617
        elif unit_out == 'c/pa':
            rJouleTCOut = jouthcsi - 273.15
        elif unit_out == 'c/kpa':
            rJouleTCOut = (jouthcsi - 273.15)/ 1.e-3
        elif unit_out == 'c/mpa':
            rJouleTCOut = (jouthcsi - 273.15) / 1.e-6
        elif unit_out == 'c/atm':
            rJouleTCOut = (jouthcsi - 273.15) / 9.86923266716013e-6
        elif unit_out == 'c/bar':
            rJouleTCOut = (jouthcsi - 273.15) / 1.e-5
        elif unit_out == 'c/psi':
            rJouleTCOut = (jouthcsi - 273.15) / 1.45037737730209e-4
        elif unit_out == 'c/torr':
            rJouleTCOut = (jouthcsi - 273.15) / 0.007500617
        elif unit_out == 'c/mmhg':
            rJouleTCOut = (jouthcsi - 273.15) / 0.007500617
        elif unit_out == 'f/pa':
            rJouleTCOut = 1.8 * jouthcsi - 459.67
        elif unit_out == 'f/kpa':
            rJouleTCOut = (1.8 * jouthcsi - 459.67) / 1.e-3
        elif unit_out == 'f/mpa':
            rJouleTCOut = (1.8 * jouthcsi - 459.67) / 1.e-6
        elif unit_out == 'f/atm':
            rJouleTCOut = (1.8 * jouthcsi - 459.67) / 9.86923266716013e-6
        elif unit_out == 'f/bar':
            rJouleTCOut = (1.8 * jouthcsi - 459.67) / 1.e-5
        elif unit_out == 'f/psi':
            rJouleTCOut = (1.8 * jouthcsi - 459.67) / 1.45037737730209e-4
        elif unit_out == 'f/torr':
            rJouleTCOut = (1.8 * jouthcsi - 459.67) / 0.007500617
        elif unit_out == 'f/mmHg':
            rJouleTCOut = (1.8 * jouthcsi - 459.67) / 0.007500617
        elif unit_out == 'r/pa':
            rJouleTCOut = 1.8 * jouthcsi
        elif unit_out == 'r/kpa':
            rJouleTCOut = (1.8 * jouthcsi) / 1.e-3
        elif unit_out == 'r/mpa':
            rJouleTCOut = (1.8 * jouthcsi) / 1.e-6
        elif unit_out == 'r/atm':
            rJouleTCOut = (1.8 * jouthcsi) / 9.86923266716013e-6
        elif unit_out == 'r/bar':
            rJouleTCOut = (1.8 * jouthcsi) / 1.e-5
        elif unit_out == 'r/psi':
            rJouleTCOut = (1.8 * jouthcsi) / 1.45037737730209e-4
        elif unit_out == 'r/torr':
            rJouleTCOut = (1.8 * jouthcsi) / 0.007500617
        elif unit_out == 'r/mmHg':
            rJouleTCOut = (1.8 * jouthcsi) / 0.007500617
        else:
            print('Error: No Joule Thomson Coefficient unit selected.')

        return rJouleTCOut
