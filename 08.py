# 8. Faça um Programa que pergunte quanto você ganha por hora e o  número de horas trabalhadas no
# mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Valor recebido por hora: R$ ')) # prede as informações para o usuário
horas_trabalho = float(input('Horas trabalhadas no mês: '))
salario_mes = valor_hora * horas_trabalho # faz o cálculo do salário

print(f'Salário total do mês: R${salario_mes:,.2f}') # imprime a informação