import numpy as np
from typing import Sequence

from attrs import define
from thermal.tec import tec_section, calculate_tec_section


@define(frozen=True)
class InputData:
    # Geometry
    dL_well: float
    dL_flowline: float
    dL_riser: float
    L_well: float
    L_flowline: float
    L_riser: float
    dh_well: float
    dh_flowline: float
    dh_riser: float
    ε_well: float
    ε_flowline: float
    ε_riser: float
    θ_well: float
    θ_flowline: float
    θ_riser: float
    # Thermal
    Tenv_sc: float
    Tenv_seabed: float
    Tenv_res: float
    tec_sections: Sequence[tec_section]
    # Operational
    Q_sc: float
    P_res: float
    T_res: float
    IP: float
    # PVT
    API: float
    dg: float
    RGO: float


@define(frozen=True)
class OperationalData:
    Q_sc: float
    P_res: float
    T_res: float


@define(frozen=True)
class GeometryData:
    dh: float
    εr: float
    θ: float
    tec: float
    T_env: float


@define(frozen=True)
class FlowData:
    Q: float


@define(frozen=True)
class MeshData:
    geometry: GeometryData
    dL: float
    MDi: float
    MDf: float


def building_mesh(data: InputData) -> list[MeshData]:
    full_mesh_list = []

    # System data
    sections_well = np.ceil(data.L_well / data.dL_well)
    sections_flowline = np.ceil(data.L_flowline / data.dL_flowline)
    sections_riser = np.ceil(data.L_riser / data.dL_riser)

    L_total = data.L_well + data.L_flowline + data.L_riser

    # Auxiliary functions
    def calculate_env_temperature_gradient(
        T_env_top: float, T_env_button: float, L_section: float
    ) -> float:
        return (T_env_top - T_env_button) / L_section

    def calculate_env_temperature(MD: float, T_button: float, T_grad: float) -> float:
        return T_button + T_grad * MD

    def get_section_tec(MD: float, tec_sections: Sequence[tec_section]) -> float:
        N_sections = len(tec_sections)
        tec = np.nan

        for sec in range(N_sections):
            mdi = tec_sections[sec].mdi
            mdf = tec_sections[sec].mdf

            if mdi <= MD < mdf:
                tec = calculate_tec_section(tec_sections[sec])
                break
            else:
                continue

        return tec

    # Well section data
    dL = data.dL_well
    L_well = data.L_well
    dh_well = data.dh_well
    θ_well = data.θ_well
    ε_well = data.ε_well
    T_grad_well = calculate_env_temperature_gradient(
        T_env_top=data.Tenv_seabed, T_env_button=data.Tenv_res, L_section=data.L_well
    )
    T_well_button = InputData.Tenv_res

    # Well Section
    MDi = 0
    MDf = 0

    for i in range(0, sections_well):
        MDi = MDf

        MDf = MDi + dL

        if MDf > L_well:
            dL = L_well - MDi
            MDf = L_well

        # Hydraulic diameter [m]
        dh = dh_well

        # Relative rugosity [-].
        εr = ε_well / dh

        # Inclination [rad]
        θ = np.deg2rad(θ_well)

        tec = get_section_tec(MD=MDi, tec_sections=InputData.tec_sections)

        T_env = calculate_env_temperature(
            MD=MDf, T_button=T_well_button, T_grad=T_grad_well
        )

        geometry = GeometryData(dh=dh, εr=εr, θ=θ, tec=tec, T_env=T_env)

        mesh = MeshData(geometry=geometry, dL=dL, MDi=MDi, MDf=MDf)

        full_mesh_list.append(mesh)

    return full_mesh_list


def test_well() -> None:
    assert 1 == 1
