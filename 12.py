# 12. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule
# seu peso ideal, usando a seguinte fórmula: $P = 72,7h - 58$

h = float(input('Altura (em metros): ')) # pede a informação para o usuário
p = (72.7 * h) - 58 # formula para calular o peso ideal

print(f'O peso ideal para uma pessoa desta altura é: {p:.2f} kg') # imprime as informações