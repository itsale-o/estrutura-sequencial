# 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura
# em graus Celsius. $C = \frac{5}{9}(F-32)

F = float(input('Temperatura (em °F): ')) # pede a informação para o usuário
C = (5*(F - 32)) / 9 # fórmula para converter graus fahrenheit para graus celsius

print(f'Temperatura: {C:.1f} °C') # imprime a informação na tela