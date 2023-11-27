from main import run_analysis

from fixtures import base_case_study


def test_base_case(base_case_study) -> None:

    run_analysis(base_case_study)

    assert 1 == 1
