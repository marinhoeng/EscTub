import numpy as np
import pytest
from thermal.tec import tec_section
from mesh.mesh import building_mesh, InputData
from pvt.fluid_data import Unit


@pytest.fixture
def base_case_study() -> InputData:
    well_section_1 = tec_section(
        de=np.array([0.3175, 0.2413, 0.2159, 0.1397]),
        di=np.array([0.2413, 0.2159, 0.1397, 0.1143]),
        Nl=4,
        k_values=np.array([0.9, 45, 0.3, 45]),
        mdi=0,
        mdf=1100,
    )

    well_section_2 = tec_section(
        de=np.array([0.3556, 0.3175, 0.2413, 0.2159, 0.1397]),
        di=np.array([0.3175, 0.2413, 0.2159, 0.1397, 0.1143]),
        Nl=5,
        k_values=np.array([45, 0.9, 45, 0.3, 45]),
        mdi=1100,
        mdf=1200,
    )

    well_section_3 = tec_section(
        de=np.array([0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397]),
        di=np.array([0.3556, 0.3175, 0.2413, 0.2159, 0.1397, 0.1143]),
        Nl=6,
        k_values=np.array([0.9, 45, 0.58, 45, 0.3, 45]),
        mdi=1200,
        mdf=1900,
    )

    well_section_4 = tec_section(
        de=np.array([0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397]),
        di=np.array([0.3556, 0.3175, 0.2413, 0.2159, 0.1397, 0.1143]),
        Nl=6,
        k_values=np.array([0.58, 45, 0.58, 45, 0.3, 45]),
        mdi=1900,
        mdf=2200,
    )

    well_section_5 = tec_section(
        de=np.array([0.6858, 0.508, 0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397]),
        di=np.array([0.508, 0.4064, 0.3556, 0.3175, 0.2413, 0.2159, 0.1397, 0.1143]),
        Nl=8,
        k_values=np.array([0.9, 45, 0.58, 45, 0.58, 45, 0.3, 45]),
        mdi=2200,
        mdf=3110,
    )

    well_section_6 = tec_section(
        de=np.array(
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
        di=np.array(
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
        Nl=10,
        k_values=np.array([0.9, 45, 0.9, 45, 0.58, 45, 0.58, 45, 0.3, 45]),
        mdi=3110,
        mdf=3200,
    )

    flowline = tec_section(
        de=np.array([0.3432, 0.3352, 0.2098, 0.2044, 0.2038, 0.2032]),
        di=np.array([0.3352, 0.2098, 0.2044, 0.2038, 0.2032, 0.1524]),
        Nl=6,
        k_values=np.array([0.2250, 0.1680, 0.2250, 0.2250, 0.2940, 45.0]),
        mdi=3200,
        mdf=5000,
    )

    riser = tec_section(
        de=np.array([0.3490, 0.3410, 0.1956, 0.1902, 0.1896, 0.1890]),
        di=np.array([0.3410, 0.1956, 0.1902, 0.1896, 0.1890, 0.1524]),
        Nl=6,
        k_values=np.array([0.2250, 0.1680, 0.2250, 0.2250, 0.2940, 45.0]),
        mdi=5000,
        mdf=7000,
    )

    return InputData(
        # Geometry
        dL_well=100,
        dL_flowline=100,
        dL_riser=100,
        L_well=3200,
        L_flowline=1800,
        L_riser=2000,
        dh_well=0.1524,
        dh_flowline=0.1524,
        dh_riser=0.1524,
        ε_well=0.0007,
        ε_flowline=0.0007,
        ε_riser=0.0007,
        θ_well=90,
        θ_flowline=0,
        θ_riser=90,
        # Thermal
        Tenv_sc=303.15,
        Tenv_seabed=277.15,
        Tenv_res=353.15,
        tec_sections=[
            well_section_1,
            well_section_2,
            well_section_3,
            well_section_4,
            well_section_5,
            well_section_6,
            flowline,
            riser,
        ],
        # Operational
        Q_sc=0.011574 * 3,
        P_res=600e5,
        T_res=370,
        IP=Unit.mCalc_Conv_IP(4000, 'm3/(kpa·d)', 'm3/(pa·s)'),
        # PVT
        API=35,
        dg=0.725,
        RGO=1220,
    )


def test_well(base_case_study) -> None:
    mesh = building_mesh(data=base_case_study)
    sz = len(mesh)

    assert mesh[sz - 1].MDf == 7000
    assert mesh[sz - 1].geometry.T_env == base_case_study.Tenv_sc
