# ----------------------- Questão 4 -----------------------
# Descrição do programa: O objetivo deste programa é reali-
# zar o cálculo das grandezas de uma fila M/M/s, de acordo
# com o que foi visto em sala de aula, a fim de efetuar uma
# análise comparativa entre os resultados obtidos para cada
# valor de s, em diferentes casos de teste.
# ---------------------------------------------------------
# Autores (Números de matrícula):
#   Cristhian Sala Minoves (20183005167)
#   Guilherme Moreira de Carvalho (20183017767)
#   Rafael Willian Silva (201712040162)

import numpy as np

class MMsQueue:
    def __init__(self, arrival_rate, service_rate, s):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.s = s

    def P0(self):
        return 0
    
    def P1(self):
        return 0
    
    def P2(self):
        return 0
    
    def P5(self):
        return 0
    
    def P10(self):
        return 0
    
    def L(self):
        return 0
    
    def Lq(self):
        return 0

    def W(self):
        return 0
    
    def Wq(self):
        return 0
    
    def P_Wq_more_than_0(self):
        return 0
    
    def P_Wq_more_than_1(self):
        return 0
    
    def P_Wq_more_than_2(self):
        return 0
    
    def P_Wq_more_than_4(self):
        return 0

# Função que imprime a tabela com os dados computados de forma comparativa
def print_table(columns, data):
    print(''.join(['{:>12}'.format(c) for c in columns]))
    for row in data:
        print(''.join(['{:>12}'.format('{:.3f}'.format(c)) for c in row]))

def main():
    # Variáveis iniciais e casos de teste
    s_values = (1, 2, 3, 4)
    test_cases = [
        (0.3, 0.30),
        (0.3, 0.25),
        (0.3, 0.20)
    ]

    # Declaração das colunas da tabela
    columns = ('s', 'P0', 'P1', 'P2', 'P5', 'P10', 'L', 'Lq', 'W', 'Wq', 'P(Wq > 0)', 'P(Wq > 1)', 'P(Wq > 2)', 'P(Wq > 4)')

    print('Questão 4: Cálculo das grandezas de uma fila M/M/s.')

    # Realiza as operações para cada caso de teste
    for test_case in test_cases:
        print(f'\nIniciando os cálculos para \u03BB={test_case[0]} e \u03BC={test_case[1]} e s={s_values}:\n')

        arrival_rate = test_case[0]
        service_rate = test_case[1]

        data = []

        # Chama os métodos da classe MMsQueue para computar os dados
        for s in s_values:
            queue = MMsQueue(arrival_rate, service_rate, s)
            row_data = [
                s,
                queue.P0(),
                queue.P1(),
                queue.P2(),
                queue.P5(),
                queue.P10(),
                queue.L(),
                queue.Lq(),
                queue.W(),
                queue.Wq(),
                queue.P_Wq_more_than_0(),
                queue.P_Wq_more_than_1(),
                queue.P_Wq_more_than_2(),
                queue.P_Wq_more_than_4()
            ]
            data.append(row_data)

        # Imprime a tabela a partir dos dados computados
        print_table(columns, data)
        
    return

main()