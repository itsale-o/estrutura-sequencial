# 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros
# quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário
# a quantidades de latas de tinta a serem compradas e o preço total.

area = float(input('Área a ser printada (m²): ')) # pede a informação para o usuário
latas = (area / 54) # uma lata de tinta pinta 54m²
preco = latas * 80 # calcula o preço das latas
if latas == round(latas): # round --> arredonda o valor de latas para um número inteiro
    print(f'Serão necessárias {latas:.0f} latas de tinta\nValor total: R$ {preco:.2f}')
else:
    latas = round(latas + 0.5) #round + 0.5 vai arredondar o valor para cima
    preco = latas * 80 # calcula o preço a ser pago nas latas
    print(f'Serão necessárias {latas:.0f} latas de tinta\nValor total: R$ {preco:.2f}')