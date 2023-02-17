# 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros
# quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros
# quadrados e que a tinta é vendida em latas de 18 litros, que custam 80,00 ou em galões de 3,6 litros,
# que custam 25,00. Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços
# em 3 situações:
# - comprar apenas latas de 18 litros;
# - comprar apenas galões de 3,6 litros;
# - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga
# e sempre arredonde os valores para cima, isto é, considere latas cheias.

area = float(input('Área a ser printada (m²): '))
litros_tinta = area / 6 # calcula a quantidade de tinta necessária para pintar a área informada pelo usuário

# comprando apenas latas
if litros_tinta % 18 > 0: # % representa o resto da divisão por 18
    latas = (litros_tinta // 18) + 1 # calcula a quantidade de latas necessárias e acrescenta mais uma
else:
    latas = litros_tinta // 18 # // --> representa a parte inteira da divisão por 18
preco = latas * 80
print(f'Serão necessárias {latas:.0f} lata(s)\nValor Total: R$ {preco:.2f}')

# comprando apenas galões
if litros_tinta % 3.6 > 0:
    galoes = (litros_tinta // 3.6) + 1 # calcula a quantidade de galões de tinta e acrescenta mais um
else:
    galoes = litros_tinta // 3.6 # // --> mesmo conceito usado na linha 18
preco = galoes * 25
print(f'Serão necessários {galoes:.0f} galões\nValor Total: R$ {preco:.2f} no total')

# comprando galões + latas

# acrescentamos a folga de 10%
litros_folga = litros_tinta * 1.1
galoes = 0

# só latas inteiras
latas = litros_folga // 18

# aqui vemos a tinta que faltou que não cabe em uma lata completa
tinta_faltante = litros_folga - 18 * latas

# tinta faltante em galões
if tinta_faltante > 0:
    if tinta_faltante % 3.6 > 0:
        faltante_galoes = tinta_faltante // 3.6 + 1
    else:
        faltante_galoes = tinta_faltante // 3.6
    if faltante_galoes <= 3:
        galoes = faltante_galoes
    else:
        galoes = 0
        latas = latas + 1

preco = latas * 80 + galoes * 25
print(f'São necessários {latas:.0f} latas e {galoes:.0f} galões\nValor Total: R$ {preco}')