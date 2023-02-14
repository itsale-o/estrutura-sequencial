#!/usr/bin/env python
# coding: utf-8

# # Lista de Estrutura Sequencial

# #### 1. Faça um Programa que mostre a mensagem (print) "Alô, mundo" na tela.

# In[ ]:


print('Alô, mundo')


# #### 2. Faça um Programa que peça um número (input) e então mostre a mensagem: "O número informado foi [número]."

# In[ ]:


num = input('Insira um número: ')
print(f'O número inserido foi: {num}')


# #### 3. Faça um Programa que peça dois números e imprima a soma.

# In[ ]:


num1 = float(input('Insira um número: '))
num2 = float(input('Insira outro número: '))

print(f'A soma dos números é: {num1 + num2}')


# #### 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.

# In[ ]:


nota1 = float(input('Nota 1: '))
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
media = (nota1 + nota2 + nota3 + nota4) / 4

print(f'Média Final: {media:.1f}')


# #### 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros para o usuário (input).

# In[ ]:


m = float(input('Insira uma medida (em m): '))
cm = m * 100

print(f'A medida equivale a {cm:.2f} cm')


# #### 6. Faça um Programa que peça o raio de um círculo, calcule e mostre sua área

# In[ ]:


import math

raio = float(input('Raio do círculo: '))
pi = math.pi
area = pi * (raio**2)

print(f'Área do círculo: {area:.2f}')


# #### 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário

# In[ ]:


lado = float(input('Lado do quadrado: '))
area = lado ** 2
dobro_area = area * 2

print(f'Área: {area:.2f}')
print(f'Dobro da área: {dobro_area:.2f}')


# #### 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

# In[ ]:


valor_hora = float(input('Valor recebido por hora: R$ '))
horas_trabalho = float(input('Horas trabalhadas no mês: '))
salario_mes = valor_hora * horas_trabalho

print(f'Salário total do mês: R${salario_mes:,.2f}')


# #### 9. Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
# $C = \frac{5}{9}(F-32)$

# In[ ]:


F = float(input('Temperatura (em °F): '))
C = (5*(F - 32)) / 9

print(f'Temperatura: {C:.1f} °C')


# #### 10. Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
# $F = \frac{9}{5}C + 32$

# In[ ]:


C = float(input('Temperatura (em °C): '))
F = ((9 * C) / 5) + 32

print(f'Temperatura: {F:.1f} °F')


# #### 11. Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# 
# - a) o produto do dobro do primeiro com metade do segundo
# - b) a soma do triplo do primeiro com o terceiro

# In[ ]:


num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
num3 = float(input('Terceiro número: '))
a = (2 * num1) * (num2 / 2)
b = (3 * num1) + num3

print(f'Produto do dobro do primeiro número com metade do segundo: {a:.0f}')
print(f'Soma do triplo do primeiro com o terceiro: {b:.0f}')


# #### 12. Tendo como dados de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
# $P = 72,7h - 58$

# In[ ]:


h = float(input('Altura (em metros): '))
p = (72.7 * h) - 58

print(f'O peso ideal para uma pessoa desta altura é: {p:.2f} kg')


# #### 13. Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# ##### a. Para homens: $P = 72,7h - 58$
# ##### b. Para mulheres: $P = 62,1h - 44,7$

# In[ ]:


h = float(input('Altura (em metros): '))
p_mulheres = (62.1 * h) - 44.7
p_homens = (72.7 * h) - 58

print(f'O peso ideal para uma mulher com esta altura é: {p_mulheres:.2f} kg')
print(f'O peso ideal para um homem com esta altura é: {p_homens:.2f} kg')


# #### 14. João Papo-de-Pescador, homem de bem
# 
# Comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o establecido pelo regulamento de pesca do estado de São Paulo (50 kg) deve pagar uma multa de R$ 4,00 por quilo excedente.
# 
# João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João devrá pagar. Imprima com as mensagens adequadas.

# In[ ]:


peso = float(input('Peso de peixes (em kg): '))

if peso <= 50:
    print('Não houve excesso de peso portanto não haverá multa')
else:
    excesso = peso - 50
    multa = excesso * 4
    print(f'Peso de peixes: {peso:.2f} kg\nExcesso: {excesso:.2f} kg\nMulta a pagar: R$ {multa:.2f}')


# #### 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.

# In[ ]:


valor_hora = float(input('Valor pago por hora trabalhada: '))
horas = float(input('Horas trabalhadas este mês: '))


# #####  Calcule o salário bruto (horas * salario por hora)

# In[ ]:


salario_bruto = valor_hora * horas


# ##### Calcule o desconto do IR (11% do salário bruto)

# In[ ]:


ir = salario_bruto * 0.11


# ##### Calcule o desconto do INSS (8% do salário bruto)

# In[ ]:


inss = salario_bruto * 0.08


# ##### Calcule o desconto do sindicato (5% do salário bruto)

# In[ ]:


sindicato = salario_bruto * 0.05


# ##### Calcule o salário líquido (salário bruto - descontos)

# In[ ]:


salario_liquido = salario_bruto - (ir + inss + sindicato)

print(f'+ Salário Bruto: R$ {salario_bruto:.2f}\n- IR (11%): R$ {ir:.2f}\n- INSS (8%): R$ {inss:.2f}\n- Sindicato (5%): R$ {sindicato:.2f}\n= Salário Líquido: R$ {salario_liquido:.2f}')


# #### 16. Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R\$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

# In[ ]:


area = float(input('Área a ser printada (m²): '))
latas = (area / 54) # uma lata de tinta pinta 54m²  
preco = latas * 80
if latas == round(latas): 
    print(f'Serão necessárias {latas:.0f} latas de tinta\nValor total: R$ {preco:.2f}')
else:
    latas = round(latas + 0.5) #round + 0.5 vai arredondar o valor para cima
    preco = latas * 80
    print(f'Serão necessárias {latas:.0f} latas de tinta\nValor total: R$ {preco:.2f}')


# #### 17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
# 
# Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam 80,00 ou em galões de 3,6 litros, que custam 25,00.
# Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
# - comprar apenas latas de 18 litros;
# - comprar apenas galões de 3,6 litros;
# - misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

# In[ ]:


area = float(input('Área a ser printada (m²): '))
litros_tinta = area / 6

# comprando apenas latas
if litros_tinta % 18 > 0: # % representa o resto da divisão
    latas = (litros_tinta // 18) + 1
else:
    latas = litros_tinta // 18
preco = latas * 80
print(f'Serão necessárias {latas:.0f} lata(s)\nValor Total: R$ {preco:.2f}')


# #### Comprando apenas galões

# In[ ]:


if litros_tinta % 3.6 > 0:
    galoes = (litros_tinta // 3.6) + 1
else:
    galoes = litros_tinta // 3.6
preco = galoes * 25
print(f'Serão necessários {galoes:.0f} galões\nValor Total: R$ {preco:.2f} no total')


# #### Comprando latas + galões

# In[ ]:


# comprando latas + galões

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


# #### 18. Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
# 
# Detalhe: MB significa megabyte, Mb (com b minúsculo) significa megabit. Um megabit é 1/8 de um megabyte. 

# In[ ]:


tamanho = float(input('Informe o tamanho do arquivo em MB: '))
velocidade = float(input('Informe a velocidade da conexão em Mbps: '))

# aqui trasnformamos megabytes em megabits para que tamanho e velocidade estejam na mesma unidade
tamanho_megabits = tamanho * 8
tempo = tamanho_megabits / velocidade
# transformando em minutos
tempo_minutos = tempo / 60
print(f'O tempo de download é de {tempo_minutos:.1f} minutos')

