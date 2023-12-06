# ----------------------- Questão 2 -----------------------
# Descrição do programa: O programa simula transições por 5 estados
# de acordo com a probabilidade de avançar ou regredir para avaliar
# a proporção de finalizações nos estados 0 ou 4 absorventes
# ---------------------------------------------------------
# Autores (Números de matrícula):
#   Cristhian Sala Minoves (20183005167)
#   Guilherme Moreira de Carvalho (20183017767)
#   Rafael Willian Silva (201712040162)

import numpy as np
import random

MAX_ITERATIONS = 1000
N = 100

start = 0   # estado inicial de uma simulação
p10 = 0
p20 = 0
p30 = 0     # pij: qtd de finalizações em j
p14 = 0     # partindo de i
p24 = 0
p34 = 0

def step(i):
    global p10, p20, p30, p14, p24, p34

    x = random.random()
    # roleta: probabilidade de "ganhar" ou "perder"
    if (x <= 0.33333):
        i = i + 1
    else:
        i = i - 1

    # acompanhamento do fim das transições de acordo
    # com o estado inicial
    if (i == 0):
        if (start == 1): p10 = p10 + 1
        elif (start == 2): p20 = p20 + 1
        else: p30 = p30 + 1
 
    elif (i == 4):
        if (start == 1): p14 = p14 + 1
        elif (start == 2): p24 = p24 + 1
        else: p34 = p34 + 1

    return i

def main():
    global start, p10, p20, p30, p14, p24, p34

    for it in range(MAX_ITERATIONS):
        i = random.randint(1, 3)
        start = i
        for n in range(N):
            i = step(i)
            if (i == 0 or i == 4):
                break

    p10 = p10 / 1000
    p20 = p20 / 1000
    p30 = p30 / 1000
    p14 = p14 / 1000
    p24 = p24 / 1000
    p34 = p34 / 1000
    sum0 = p10 + p20 + p30
    sum4 = p14 + p24 + p34

    # impressão da saída
    print(''.join(['{:>12}'.format(c) for c in ('', 0, 4)]))
    for row in [[1, p10, p14], [2, p20, p24], [3, p30, p34]]:
        print(''.join(['{:>12}'.format('{:.3f}'.format(c)) for c in row]))
    print(''.join(['{:>12}'.format(c) for c in ('Total', sum0, sum4)]))

    return

main()
