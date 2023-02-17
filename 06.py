# 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área

import math # importa o pacote com funções matemáticas

raio = float(input('Raio do círculo: ')) # pede a informação para o usuário
pi = math.pi # o número pi importado da função math
area = pi * (raio**2) # calcule a área do círculo

print(f'Área do círculo: {area:.2f}') # imprime a informação na tela