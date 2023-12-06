import numpy as np
from typing import Sequence
from attrs import define
from src.thermal.tec import tec_section, calculate_tec_section


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
    IP: float


@define(frozen=True)
class FlowData:
    Qm: float
    Vm: float
    Vsl: float
    Vsg: float
    λL: float
    HL: float


@define(frozen=True)
class GeometryData:
    dh: float
    εr: float
    θ: float
    tec: float
    T_env: float


@define(frozen=True)
class MeshData:
    geometry: GeometryData
    dL: float
    MDi: float
    MDf: float


def building_mesh(data: InputData) -> list[MeshData]:
    full_mesh_list = []

    # Auxiliary functions
    def calculate_env_temperature_gradient(
            T_env_top: float, T_env_button: float, TVD_section: float
    ) -> float:
        return (T_env_top - T_env_button) / TVD_section

    def calculate_env_temperature(TVD: float, T_button: float, T_grad: float) -> float:
        return T_button + T_grad * TVD

    def get_section_tec(
            MD_start: float, MD_end: float, tec_sections: Sequence[tec_section]
    ) -> float:
        N_sections = len(tec_sections)
        tec_calc = np.nan

        for sec in range(N_sections):
            mdi = tec_sections[sec].mdi
            mdf = tec_sections[sec].mdf

            if mdi <= MD_start < mdf:
                tec_calc = calculate_tec_section(tec_sections[sec])
                break
            else:
                continue

        return tec_calc

    # Well section data
    sections_well = int(np.ceil(data.L_well / data.dL_well))
    sections_flowline = int(np.ceil(data.L_flowline / data.dL_flowline))
    sections_riser = int(np.ceil(data.L_riser / data.dL_riser))

    T_grad_well = calculate_env_temperature_gradient(
        T_env_top=data.Tenv_seabed, T_env_button=data.Tenv_res, TVD_section=data.L_well
    )

    T_grad_flowline = 0.0

    T_grad_riser = calculate_env_temperature_gradient(
        T_env_top=data.Tenv_sc, T_env_button=data.Tenv_seabed, TVD_section=data.L_riser
    )

    sec_number = [
        0,
        sections_well,
        sections_well + sections_flowline,
        sections_well + sections_flowline + sections_riser,
    ]
    sec_L = [
        data.L_well,
        data.L_well + data.L_flowline,
        data.L_well + data.L_flowline + data.L_riser,
    ]
    sec_dL = [data.dL_well, data.dL_flowline, data.dL_riser]
    sec_dh = [data.dh_well, data.dh_flowline, data.dh_riser]
    sec_θ = [data.θ_well, data.θ_flowline, data.θ_riser]
    sec_ε = [data.ε_well, data.ε_flowline, data.ε_riser]
    sec_T_button = [data.Tenv_res, data.Tenv_seabed, data.Tenv_seabed]
    sec_T_grad = [T_grad_well, T_grad_flowline, T_grad_riser]

    MDf = 0
    for k in range(0, 3):
        dL = sec_dL[k]
        for i in range(sec_number[k], sec_number[k + 1]):
            # Initial and Final positions of the actual section [m].
            MDi = MDf
            MDf = MDi + dL

            if MDf > sec_L[k]:
                dL = sec_L[k] - MDi
                MDf = sec_L[k]

            # Hydraulic diameter [m].
            dh = sec_dh[k]

            # Relative rugosity [-].
            εr = sec_ε[k] / sec_dh[k]

            # Inclination [rad].
            θ = np.deg2rad(sec_θ[k])

            if k == 0:  # well
                δ_TVD = MDf
            elif k == 1:  # flowline
                δ_TVD = sec_L[0]
            else:  # riser
                δ_TVD = MDf - sec_L[1]

            # Thermal Exchange Coefficient [].
            tec = get_section_tec(
                MD_start=MDi, MD_end=MDf, tec_sections=data.tec_sections
            )

            # Environment temperature [K].
            T_env = calculate_env_temperature(
                TVD=δ_TVD, T_button=sec_T_button[k], T_grad=sec_T_grad[k]
            )

            # Saving the geometry data
            geometry = GeometryData(dh=dh, εr=εr, θ=θ, tec=tec, T_env=T_env)

            # Saving the mesh data
            mesh = MeshData(geometry=geometry, dL=dL, MDi=MDi, MDf=MDf)

            full_mesh_list.append(mesh)

    return full_mesh_list
