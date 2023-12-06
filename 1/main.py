# ----------------------- Questão 1 -----------------------
# Descrição do programa: Código que encontra a solução de
# um jogo de soma zero, utilizando programação linear.
# ---------------------------------------------------------
# Autores (Números de matrícula):
#   Cristhian Sala Minoves (20183005167)
#   Guilherme Moreira de Carvalho (20183017767)
#   Rafael Willian Silva (201712040162)

from scipy.optimize import linprog
import numpy as np

MAX_SIMULATIONS = 100

# Resolve um jogo e retorna o valor do jogo, o array de probabilidades e a mensagem de status da solução
def solve_game(prizes_matrix):
    pure_prizes_matrix = remove_dominated_strategies(prizes_matrix)
    c, A_ub, b_ub, A_eq, b_eq, bounds = get_problem_parameters_from_prizes(pure_prizes_matrix)
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    return res.fun, res.x[:len(prizes_matrix[0])], pure_prizes_matrix

# Remove as estratégias dominadas de uma matriz de prêmios
def remove_dominated_strategies(prizes_matrix):
    num_rows = len(prizes_matrix)
    num_cols = len(prizes_matrix[0])

    rows_to_remove = []
    columns_to_remove = []

    # Econtra as linhas que devem ser eliminadas
    for i in range(num_rows):
        for j in range(num_rows):
            if i != j:
                total_domination = 0
                for k in range(num_cols):
                    if prizes_matrix[i][k] > prizes_matrix[j][k]:
                        total_domination += 1
                if total_domination == num_cols and j not in rows_to_remove:
                    rows_to_remove.append(j)

    # Mapeia a matriz de prêmios para uma matriz de prêmios negativos
    b_prizes_matrix = []
    for i in range(num_rows):
        b_prizes_matrix.append([])
        for j in range(num_cols):
            b_prizes_matrix[i].append(prizes_matrix[i][j] * -1)

    # Encontra as colunas que devem ser eliminadas
    for i in range(num_cols):
        for j in range(num_cols):
            if i != j:
                total_domination = 0
                for k in range(num_rows):
                    if b_prizes_matrix[k][i] > b_prizes_matrix[k][j]:
                        total_domination += 1
                if total_domination == num_rows and j not in columns_to_remove:
                    columns_to_remove.append(j)

    # Cria uma nova matriz de prêmios sem as linhas e colunas dominadas
    new_prizes_matrix = []
    for i in range(num_rows):
        if i not in rows_to_remove:
            new_prizes_matrix.append([])
            for j in range(num_cols):
                if j not in columns_to_remove:
                    new_prizes_matrix[-1].append(prizes_matrix[i][j])
    
    return new_prizes_matrix

# Realiza a simulação de um jogo dadas as probabilidades e a matriz de prêmios sem estratégias dominadas
def simulate(pure_prizes_matrix, probabilities):
    a_prizes = 0
    b_prizes = 0

    for _ in range(MAX_SIMULATIONS):
        col = np.random.choice(np.arange(0, len(pure_prizes_matrix[0])), p=probabilities)
        # Presumimos que o segundo jogador não conhece a estratégia selecionada pelo primeiro
        a_selection = np.random.randint(0, len(pure_prizes_matrix))
        best_prize_for_a = pure_prizes_matrix[a_selection][col]
        a_prizes += best_prize_for_a
        b_prizes -= pure_prizes_matrix[a_selection][col]

    return a_prizes, b_prizes

# Retorna os parâmetros do problema de programação linear
def get_problem_parameters_from_prizes(prizes_matrix):
    num_rows = len(prizes_matrix[0])

    c = ([0] * num_rows) + [1]

    A_ub = []
    for row in prizes_matrix:
        coef = []
        for i in range(len(row)):
            coef.append(row[i])
        coef.append(-1)
        A_ub.append(coef)

    b_ub = [0] * len(prizes_matrix)
    A_eq = ([1] * num_rows) + [0]
    b_eq = [1]

    bounds = []
    for _ in range(num_rows):
        bounds.append((0, None))
    bounds.append((None, None))

    return c, A_ub, b_ub, [A_eq], b_eq, bounds

def main():
    problem_b = [[1,-1], [-1,1]]
    problem_c = [[3, -1, -3], [-2, 4, -1], [-5, -6, -2]]

    print('-------------------------------------------------------------')
    print('Resolvendo a questão 1.b.')

    prize_sum = 0
    _, probabilities, pure_prize_matrix = solve_game(problem_b)
    print(probabilities)
    print(pure_prize_matrix)
    a_prize, _ = simulate(pure_prize_matrix, probabilities)
    prize_sum += a_prize
    
    print('\nPrêmio acumulado ao final de 100 iterações: ', prize_sum)
    print('-------------------------------------------------------------')
    print('Resolvendo a questão 1.c.\n\n(i) Tabela de prêmios:\n')
    for i in range(len(problem_c)):
        print(problem_c[i])

    prize, probabilities, pure_prizes_matrix = solve_game(problem_c)
    print('\nPrêmio: ', prize)
    print('Probabilidades: ', probabilities)

    print('\n(ii) Simulando o jogo para a solução ótima 100 vezes')
    a_prizes, b_prizes = simulate(pure_prizes_matrix, probabilities)
    print('Prêmio acumulado para A: ', a_prizes)
    print('Prêmio acumulado para B: ', b_prizes)

    probabilities[0] -= 0.01
    probabilities[2] += 0.01

    print('\n(iii) Simulando o jogo para a solução modificada 100 vezes')
    a_prizes_modified, b_prizes_modified = simulate(pure_prizes_matrix, probabilities)
    print('Prêmio acumulado para A: ', a_prizes_modified)
    print('Prêmio acumulado para B: ', b_prizes_modified)

    print('\n(iv) Comparando os resultados')
    print('Diferença do prêmio acumulado para A: ', a_prizes_modified - a_prizes)
    print('Diferença do prêmio acumulado para B: ', b_prizes_modified - b_prizes)

    return

main()