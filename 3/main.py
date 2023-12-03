# ----------------------- Questão 3 -----------------------
# Descrição do programa: Programa criado para simular um
# sistema de filas com um número de servidores, uma taxa de
# chegada e uma taxa de serviço variáveis, de acordo com os
# casos de teste propostos. A letra a da questão é apenas a
# criação da função simulate, que simula o sistema de filas
# e a letra b é a criação dos casos de teste e a execução
# das simulações.
# ---------------------------------------------------------
# Autores (Números de matrícula):
#   Cristhian Sala Minoves (20183005167)
#   Guilherme Moreira de Carvalho (20183017767)
#   Rafael Willian Silva (201712040162)

import numpy as np
import matplotlib.pyplot as plt

MAX_RANDOM_VALUE = 1
MIN_RANDOM_VALUE = 0
TOTAL_ITERATIONS = 1000
TOTAL_SIMULATIONS = 100

# Simula o sistema de filas
# [arrival_rate]: Taxa de chegada (lambda)
# [service_rate]: Taxa de serviço (mu)
# [s]: Número de servidores
# [T]: Tempo de simulação (Número de iterações)
def simulate(arrival_rate, service_rate, s, T):
    # Adiciona os vetores de controle da simulação
    queue = []
    waiting_customers = []
    total_customers = []

    attendants = []
    for i in range(s):
        # Adiciona um atendente livre (0... e sem tempo de serviço remanescente ..., 0)
        attendants.append((0, 0)) 

    # Simula o sistema de filas por T unidades de tempo
    for i in range(T):
        # Checa se algum cliente chegou
        should_arrive_new_customer = np.random.uniform(MIN_RANDOM_VALUE, MAX_RANDOM_VALUE) < arrival_rate
        if should_arrive_new_customer:
            queue.append(i)
        
        # Verifica se algum atendente está+ livre
        for j in range(len(attendants)):
            if attendants[j][0] == 0:
                # Verifica se existe alguém na fila
                if len(queue) > 0:
                    # Remove o primeiro cliente da fila
                    queue.pop(0)
                    # Cria uma tupla de atendente ocupado (1, iterações para finalizar o atendimento)
                    attendant = (1, np.rint(1/service_rate))
                    # Atualiza o estado do atendente
                    attendants[j] = attendant
            else:
                remaining_service_time = attendants[j][1] - 1
                if remaining_service_time <= 0:
                    # Atendente está livre
                    attendant = (0, 0)
                    # Atualiza o estado do atendente
                    attendants[j] = attendant
                else:
                    # Atualiza o tempo de serviço remanescente do atendente
                    attendants[j] = (1, remaining_service_time)
        
        # Encontra o número de atendentes ocupados
        busy_attendants = 0
        for attendant in attendants:
            if attendant[0] == 1:
                busy_attendants += 1

        # Atualiza os vetores de estado do sistema
        waiting_customers.append(len(queue))
        total_customers.append(len(queue) + busy_attendants)

    return waiting_customers, total_customers

# Salva os resultados da simulação em um arquivo png no caminho que for enviado por parâmetro
def save_simulation_results(X, Y, title, xlabel, ylabel, filepath):
    fig, ax = plt.subplots()
    ax.plot(X, Y, linewidth=1.0)
    
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    plt.savefig(filepath, dpi=300, bbox_inches='tight')

def main():
    # Criação dos casos de teste da letra b
    test_cases = [
        (0.3, 0.25, 1),
        (0.3, 0.25, 2),
        (0.3, 0.20, 3)
    ]

    # Prepara os valores do eixo X para plotar futuramente
    x = np.arange(0, TOTAL_ITERATIONS, 1)
    X = []
    for _ in range(TOTAL_SIMULATIONS):
        X.append(x)

    print('\nQuestão 3: Iniciando simulação das filas...\n')

    # Executa as simulações para cada caso de teste
    for idx, test_case in enumerate(test_cases):
        waiting_for_iteration = []
        total_for_iteration = []

        for _ in range(TOTAL_SIMULATIONS):
            waiting_customers, total_customers = simulate(test_case[0], test_case[1], test_case[2], TOTAL_ITERATIONS)
            waiting_for_iteration.append(waiting_customers)
            total_for_iteration.append(total_customers)

        # Plota os valores de usuários em espera na fila
        waiting_path = f'./results/test_case_{idx + 1}/waiting.png'
        save_simulation_results(
            X,
            waiting_for_iteration,
            f'Número de clientes na fila para \u03BB={test_case[0]}, \u03BC={test_case[1]} e s={test_case[2]}',
            'Iteração',
            'Número de clientes na fila',
            waiting_path
        )
        print('Resultado da simulação salvo em: ' + waiting_path)

        # Plota os valores de usuários em espera no sistema
        total_path = f'./results/test_case_{idx + 1}/total.png'
        save_simulation_results(
            X,
            total_for_iteration,
            f'Número de clientes no sistema para \u03BB={test_case[0]}, \u03BC={test_case[1]} e s={test_case[2]}',
            'Iteração',
            'Número de clientes no sistema',
            total_path
        )
        print('Resultado da simulação salvo em: ' + total_path)
    
    print('\nSimulação concluída, confira os resultados na pasta ./results')

    return

main()
