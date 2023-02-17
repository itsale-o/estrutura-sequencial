# 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus
# Fahrenheit. $F = \frac{9}{5}C + 32$

C = float(input('Temperatura (em °C): ')) # pede a informação para o usuário
F = ((9 * C) / 5) + 32 # fórmula para converter graus celsius para graus fahrenheit

print(f'Temperatura: {F:.1f} °F') # imprime as informações