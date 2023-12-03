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
import math

class MMsQueue:
    def __init__(self, arrival_rate, service_rate, s):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.s = s

    def P0(self):
        num = 1
        den = 0

        for n in range(self.s):
            factor1= ((self.arrival_rate / self.service_rate) ** n) / math.factorial(n)
            factor2 = ((self.arrival_rate / self.service_rate) ** self.s) / (math.factorial(self.s))
            factor3 = 1.0 / (1.0 - (self.arrival_rate / (self.s * self.service_rate)))
            den += factor1 + factor2 * factor3

        return num / den
    
    def Pn(self, n):
        if n < self.s:
            return (((self.arrival_rate / self.service_rate) ** n) / math.factorial(n)) * self.P0()
        else:
            return (((self.arrival_rate / self.service_rate) ** n) / (math.factorial(self.s) * (self.s ** (n - self.s)))) * self.P0()

    def P1(self):
        return self.Pn(1)
    
    def P2(self):
        return self.Pn(2)
    
    def P5(self):
        return self.Pn(5)
    
    def P10(self):
        return self.Pn(10)
    
    def rho(self):
        return self.arrival_rate / (self.s * self.service_rate)
    
    def L(self):
        return self.Lq() + (self.arrival_rate / self.service_rate)
    
    def Lq(self):
        num = self.P0()*((self.arrival_rate / self.service_rate) ** self.s) * self.rho()
        den = math.factorial(self.s)*((1-self.rho())**2)
        return num / den

    def W(self):
        return self.Wq() + (1 / self.service_rate)
    
    def Wq(self):
        return self.Lq() / self.arrival_rate
    
    def P_Wq_equals_0(self):
        sum = 0
        for n in range(self.s):
            if n == 0:
                sum += self.P0()
            else:
                sum += self.Pn(n)
        return sum
    
    def P_Wq_more_than_t(self, t):
        return (1 - self.P_Wq_equals_0()) * math.exp((-1 * self.s * self.service_rate) * ((1 - self.rho()) ** t))
    
    def P_Wq_more_than_0(self):
        return self.P_Wq_more_than_t(0)
    
    def P_Wq_more_than_1(self):
        return self.P_Wq_more_than_t(1)
    
    def P_Wq_more_than_2(self):
        return self.P_Wq_more_than_t(2)
    
    def P_Wq_more_than_5(self):
        return self.P_Wq_more_than_t(5)

# Função que imprime a tabela com os dados computados de forma comparativa
def print_table(columns, data):
    print(''.join(['{:>12}'.format(c) for c in columns]))
    for row in data:
        print(''.join(['{:>12}'.format('{:.3f}'.format(c)) for c in row]))

def main():
    # Variáveis iniciais e casos de teste
    s_values = (1, 2, 3, 4)
    test_cases = [
        (2, 3),
        (2, 5),
        (8, 6)
    ]

    # Declaração das colunas da tabela
    columns = ('s', 'P0', 'P1', 'P2', 'P5', 'P10', 'L', 'Lq', 'W', 'Wq', 'P(Wq > 0)', 'P(Wq > 1)', 'P(Wq > 2)', 'P(Wq > 5)')

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
                queue.P_Wq_more_than_5()
            ]
            data.append(row_data)

        # Imprime a tabela a partir dos dados computados
        print_table(columns, data)

    print('\nNeste último caso, os resultados não se aplicam em s=1, pois \u03BB > s\u03BC, fazendo com que a fila cresça indefinidamenta a longo prazo.')
    print('\nFim da execução.')
        
    return

main()