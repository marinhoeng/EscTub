import numpy as np
import TEC


class OperationalConditions:  # verificar se essa classe ficará aqui ou criaremos uma fb-operational_conditions

    def __init__(self, Tenv_sc: float, Tenv_seabed: float, Tenv_res: float, Q_sc: float, P_res: float):
        self.Tenv_sc: float = Tenv_sc
        self.Tenv_seabed: float = Tenv_seabed
        self.Tenv_res: float = Tenv_res
        self.Q_sc: float = Q_sc
        self.P_res: float = P_res


class Geometry:

    def __init__(self, dL_well: float, dL_flowline: float, dL_riser: float,
                 L_well: float, L_flowline: float, L_riser: float,
                 dh_well: float, dh_flowline: float, dh_riser: float,
                 ε_well: float, ε_flowline: float, ε_riser: float,
                 θ_well: float, θ_flowline: float, θ_riser: float):

        self.dL_well: float = dL_well
        self.dL_flowline: float = dL_flowline
        self.dL_riser: float = dL_riser

        self.L_well: float = L_well
        self.L_flowline: float = L_flowline
        self.L_riser: float = L_riser

        self.sections_well: int = np.ceil(self.L_well / self.dL_well)
        self.sections_flowline: int = np.ceil(L_flowline / self.dL_flowline)
        self.sections_riser: int = np.ceil(L_riser / self.dL_riser)

        self.L_total: float = self.L_well + self.L_flowline + self.L_riser

        self.dh_well: float = dh_well
        self.dh_flowline: float = dh_flowline
        self.dh_riser: float = dh_riser

        self.ε_well: float = ε_well
        self.ε_flowline: float = ε_flowline
        self.ε_riser: float = ε_riser

        self.θ_well: float = θ_well
        self.θ_flowline: float = θ_flowline
        self.θ_riser: float = θ_riser


# =====================================================================================================================


class Mesh:
    
    # aq apenas coloco os argumentos que compõem a malha
    # e que serão preenchidos pelo mesh_running no futuro

    def __init__(self, dh: float, dL: float, θ: float, ε: float, T_env: float, MDi: float, TEC: float):
        self.dh: float = dh
        self.dL: float = dL
        self.θ: float = θ
        self.ε: float = ε
        self.T_env: float = T_env
        self.MDi: float = MDi
        self.TEC: float = TEC


def mesh_running(gm: Geometry, op: OperationalConditions, tec: TEC):

    full_mesh_list = []

    MDi_well = np.zeros(gm.sections_well)
    dL_well = np.zeros(gm.sections_well)

    MDi_flowline = np.zeros(gm.sections_flowline)
    dL_flowline = np.zeros(gm.sections_flowline)

    MDi_riser = np.zeros(gm.sections_riser)
    dL_riser = np.zeros(gm.sections_riser)

    for i in range(1, gm.sections_well):  # trabalhando no poço

        dL_well[i] = gm.dL_well

        MDi_well[i] = MDi_well[i - 1] + gm.dL_well

        if MDi_well[i] > gm.L_well:

            dL_well[i] = gm.L_well - dL_well[i - 1]

            MDi_well[i] = gm.L_well

        dh = gm.dh_well
        θ = np.deg2rad(gm.θ_well)
        ε = gm.ε_well

        grad_T_well = (op.Tenv_seabed - op.Tenv_res) / gm.L_well
        T_env = grad_T_well * MDi_well + op.Tenv_res

        if 2100 < MDi_well <= 3200:

            TEC = TEC.tec_p1

        elif 2000 < MDi_well <= 2100:

            TEC = TEC.tec_p2

        elif 1300 < MDi_well <= 2000:

            TEC = TEC.tec_p3

        elif 1000 < MDi_well <= 1300:

            TEC = TEC.tec_p4

        elif 90 < MDi_well <= 1000:

            TEC = TEC.tec_p5

        else:

            TEC = TEC.tec_p6

    full_mesh_list.append(Mesh(dh=dh, dL=dL_well, θ=θ, ε=ε, T_env=T_env, MDi=MDi_well, TEC=TEC))

    for i in range(1, gm.sections_flowline):  # trabalhando na flowline

        dL_flowline[i] = gm.dL_flowline

        MDi_flowline[i] = MDi_flowline[i - 1] + gm.dL_flowline

        if MDi_flowline[i] > gm.L_flowline:

            dL_flowline[i] = gm.L_flowline - dL_flowline[i - 1]

            MDi_flowline[i] = gm.L_flowline

        dh = gm.dh_flowline
        θ = np.deg2rad(gm.θ_flowline)
        ε = gm.ε_flowline
        T_env = op.Tenv_seabed

        TEC_flowline = TEC.tec_f

    full_mesh_list.append(Mesh(dh=dh, dL=dL_flowline, θ=θ, ε=ε, T_env=T_env, MDi=MDi_flowline, TEC=TEC_flowline))

    for i in range(1, gm.sections_riser):  # trabalhando no riser

        dL_riser[i] = gm.dL_riser

        MDi_riser[i] = MDi_riser[i - 1] + gm.dL_riser

        if MDi_riser[i] > gm.L_riser:

            dL_riser[i] = gm.L_riser - dL_riser[i - 1]

            MDi_riser[i] = gm.L_riser

        dh = gm.dh_riser
        θ = np.deg2rad(gm.θ_riser)
        ε = gm.ε_riser

        grad_T_sea = (op.Tenv_sc - op.Tenv_seabed) / gm.L_riser
        T_env = grad_T_sea * MDi_riser + op.Tenv_seabed

        TEC_riser = TEC.tec_r

    full_mesh_list.append(Mesh(dh=dh, dL=dL_riser, θ=θ, ε=ε, T_env=T_env, MDi=MDi_riser, TEC=TEC_riser))

    return full_mesh_list
