from mesh.mesh import building_mesh
from fixtures import base_case_study


def test_well(base_case_study) -> None:
    mesh = building_mesh(data=base_case_study)
    sz = len(mesh)

    assert mesh[sz - 1].MDf == 7000
    assert mesh[sz - 1].geometry.T_env == base_case_study.Tenv_sc
