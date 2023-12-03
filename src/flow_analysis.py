from main import run_analysis
from main import ResultsData
from mesh.mesh import MeshData
from fixtures import base_case_study, base_case_study_2
import matplotlib.pyplot as plt


'''def test_base_case(base_case_study) -> None:
    results = run_analysis(base_case_study)

    plt.plot(results.Tvec, results.Pvec,label='P vs T')
    plt.xlabel('Temperature(K)')
    plt.ylabel('Pressure(Bar)')
    plt.title('Perfil Termohidráulico')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Pvec, label='Pressure vs MD')
    plt.xlabel('MD')
    plt.ylabel('Pressure')
    plt.title('Pressure vs MD')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Tvec, label='Temperature vs MD')
    plt.xlabel('MD')
    plt.ylabel('Temperature')
    plt.title('Temperature vs MD')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Pb_vec, label='Pb vs MD')
    plt.xlabel('MD')
    plt.ylabel('Pb')
    plt.title('Pressão de bolha vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Rs_vec, label='Rs vs MD')
    plt.xlabel('MD')
    plt.ylabel('Rs')
    plt.title('Razão de solubilidade vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Bo_vec, label='Bo vs MD')
    plt.xlabel('MD')
    plt.ylabel('Bo')
    plt.title('Fator volume do óleo vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.ρ_oil_vec, label='ρ_oil vs MD')
    plt.xlabel('MD')
    plt.ylabel('ρ_oil')
    plt.title('Densidade específica do óleo vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.ρ_gas_vec, label='ρ_gas vs MD')
    plt.xlabel('MD')
    plt.ylabel('ρ_gas')
    plt.title('Densidade específica do gás vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.μ_oil_vec, label='μ_oil vs MD')
    plt.xlabel('MD')
    plt.ylabel('μ_oil')
    plt.title('Viscosidade do óleo vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.μ_gas_vec, label='μ_gas vs MD')
    plt.xlabel('MD')
    plt.ylabel('μ_gas')
    plt.title('Viscosidade do gás vs Comprimento')
    plt.legend()
    plt.show()
    assert 1 == 1'''''


def test_base_case_2(base_case_study_2) -> None:
    results = run_analysis(base_case_study_2)

    plt.plot(results.Tvec, results.Pvec,label='P vs T')
    plt.xlabel('Temperature(K)')
    plt.ylabel('Pressure(Bar)')
    plt.title('Perfil Termohidráulico')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Pvec, label='Pressure vs MD')
    plt.xlabel('MD')
    plt.ylabel('Pressure')
    plt.title('Pressure vs MD')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Tvec, label='Temperature vs MD')
    plt.xlabel('MD')
    plt.ylabel('Temperature')
    plt.title('Temperature vs MD')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Pb_vec, label='Pb vs MD')
    plt.xlabel('MD')
    plt.ylabel('Pb')
    plt.title('Pressão de bolha vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Rs_vec, label='Rs vs MD')
    plt.xlabel('MD')
    plt.ylabel('Rs')
    plt.title('Razão de solubilidade vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Bo_vec, label='Bo vs MD')
    plt.xlabel('MD')
    plt.ylabel('Bo')
    plt.title('Fator volume do óleo vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.ρ_oil_vec, label='ρ_oil vs MD')
    plt.xlabel('MD')
    plt.ylabel('ρ_oil')
    plt.title('Densidade específica do óleo vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.ρ_gas_vec, label='ρ_gas vs MD')
    plt.xlabel('MD')
    plt.ylabel('ρ_gas')
    plt.title('Densidade específica do gás vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.μ_oil_vec, label='μ_oil vs MD')
    plt.xlabel('MD')
    plt.ylabel('μ_oil')
    plt.title('Viscosidade do óleo vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.μ_gas_vec, label='μ_gas vs MD')
    plt.xlabel('MD')
    plt.ylabel('μ_gas')
    plt.title('Viscosidade do gás vs Comprimento')
    plt.legend()
    plt.show()
    assert 1 == 1


def test_base_case_3(base_case_study_3) -> None:
    results = run_analysis(base_case_study_3)

    plt.plot(results.Tvec, results.Pvec, label='P vs T')
    plt.xlabel('Temperature(K)')
    plt.ylabel('Pressure(Bar)')
    plt.title('Perfil Termohidráulico')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Pvec, label='Pressure vs MD')
    plt.xlabel('MD')
    plt.ylabel('Pressure')
    plt.title('Pressure vs MD')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Tvec, label='Temperature vs MD')
    plt.xlabel('MD')
    plt.ylabel('Temperature')
    plt.title('Temperature vs MD')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Pb_vec, label='Pb vs MD')
    plt.xlabel('MD')
    plt.ylabel('Pb')
    plt.title('Pressão de bolha vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Rs_vec, label='Rs vs MD')
    plt.xlabel('MD')
    plt.ylabel('Rs')
    plt.title('Razão de solubilidade vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.Bo_vec, label='Bo vs MD')
    plt.xlabel('MD')
    plt.ylabel('Bo')
    plt.title('Fator volume do óleo vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.ρ_oil_vec, label='ρ_oil vs MD')
    plt.xlabel('MD')
    plt.ylabel('ρ_oil')
    plt.title('Densidade específica do óleo vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.ρ_gas_vec, label='ρ_gas vs MD')
    plt.xlabel('MD')
    plt.ylabel('ρ_gas')
    plt.title('Densidade específica do gás vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.μ_oil_vec, label='μ_oil vs MD')
    plt.xlabel('MD')
    plt.ylabel('μ_oil')
    plt.title('Viscosidade do óleo vs Comprimento')
    plt.legend()
    plt.show()

    plt.plot(results.MD, results.μ_gas_vec, label='μ_gas vs MD')
    plt.xlabel('MD')
    plt.ylabel('μ_gas')
    plt.title('Viscosidade do gás vs Comprimento')
    plt.legend()
    plt.show()
    assert 1 == 1
