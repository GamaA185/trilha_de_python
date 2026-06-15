import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp


A = 0.204 # taxa de alimentação
B = 0.263 # constante de reação
C = 3.78 # Fator relacionado a Volume/concentração
D = 100 # Volume inicial do reator  

T_INICIAL = 0
T_FINAL = 10_000
PONTOS = 1_000

X_INICIAL = 0
Y_INICIAL = 40


def modelo_reator(t, variaveis):
    x, y = variaveis
    denominador = (C * (D + t)) ** 2
    taxa_reacao = B * x**2 * y / denominador

    dx_dt = A - taxa_reacao
    dy_dt = -taxa_reacao

    return [dx_dt, dy_dt]


def resolver_reator():
    tempos = np.linspace(T_INICIAL, T_FINAL, PONTOS)

    solucao = solve_ivp(
        modelo_reator,
        (T_INICIAL, T_FINAL),
        [X_INICIAL, Y_INICIAL],
        t_eval=tempos,
        method="Radau",
        rtol=1e-8,
        atol=1e-10,
    )

    if not solucao.success:
        raise RuntimeError(f"Falha ao resolver o sistema: {solucao.message}")

    return solucao


def plotar_solucao(solucao):
    tempos = solucao.t
    n_b = solucao.y[1]
    n_eter = Y_INICIAL - n_b

    plt.plot(tempos, n_b, label="n_B")
    plt.plot(tempos, n_eter, label="n_eter")
    plt.xlabel("tempo / s")
    plt.ylabel("n_i / mol")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


def mostrar_resultado(solucao):
    x_final = solucao.y[0, -1]
    n_b_final = solucao.y[1, -1]
    n_eter_final = Y_INICIAL - n_b_final

    print("=== Resultado final ===")
    print(f"t = {solucao.t[-1]:.0f} s")
    print(f"x = {x_final:.6f}")
    print(f"n_B = {n_b_final:.6f} mol")
    print(f"n_eter = {n_eter_final:.6f} mol")


if __name__ == "__main__":
    solucao_reator = resolver_reator()
    mostrar_resultado(solucao_reator)
    plotar_solucao(solucao_reator)
