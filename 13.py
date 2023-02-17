# 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule
# seu peso ideal, utilizando as seguintes fórmulas:
# a. Para homens: $P = 72,7h - 58$
# b. Para mulheres: $P = 62,1h - 44,7$

h = float(input('Altura (em metros): ')) # pede as informações para o usuário
p_mulheres = (62.1 * h) - 44.7 # faz o cálculo do peso ideal para mulheres
p_homens = (72.7 * h) - 58 # faz o cálculo do peso ideal para homens

print(f'O peso ideal para uma mulher com esta altura é: {p_mulheres:.2f} kg') # imprime as informações
print(f'O peso ideal para um homem com esta altura é: {p_homens:.2f} kg')