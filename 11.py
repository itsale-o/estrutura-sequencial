# 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

# a) o produto do dobro do primeiro com metade do segundo
# b) a soma do triplo do primeiro com o terceiro

num1 = int(input('Primeiro número: ')) # pede as informações para o usuário
num2 = int(input('Segundo número: '))
num3 = float(input('Terceiro número: '))
a = (2 * num1) * (num2 / 2) # calcula o produto do dobro do primeiro número com a metade do segundo
b = (3 * num1) + num3 # calcula a soma do triplo do primeiro número com o terceiro

print(f'Produto do dobro do primeiro número com metade do segundo: {a:.0f}')
print(f'Soma do triplo do primeiro com o terceiro: {b:.0f}') # imprime as informações