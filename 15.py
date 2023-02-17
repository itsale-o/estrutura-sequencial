# 15. Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
# no mês.
# a) Calcule o salário bruto (horas * salario por hora)
# b) Calcule o desconto do IR (11% do salário bruto
# c) Calcule o desconto do INSS (8% do salário bruto)
# d) Calcule o desconto do sindicato (5% do salário bruto)
# e) Calcule o salário líquido (salário bruto - descontos)

valor_hora = float(input('Valor pago por hora trabalhada: ')) # pede as informações para o usuário
horas = float(input('Horas trabalhadas este mês: '))

# a) Cálculo do salário bruto:
salario_bruto = valor_hora * horas
# b) Cálculo do desconto do IR:
ir = salario_bruto * 0.11
# c) Cálculo do desconto do INSS:
inss = salario_bruto * 0.08
# d) Cálculo do desconto do sindicato:
sindicato = salario_bruto * 0.05
# e) Cáculo do salário líquido:
descontos = ir + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f'(+) Salário Bruto: R$ {salario_bruto:.2f}\n(-) IR (11%): R$ {ir:.2f}\n(-) INSS (8%): R$ {inss:.2f}\n(-) Sindicato (5%): R$ {sindicato:.2f}\n= Salário Líquido: R$ {salario_liquido:.2f}')