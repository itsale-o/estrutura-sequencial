# 4. Faça um Programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas.

nota1 = float(input('Nota 1: ')) # input --> pede uma informação para o usuário
nota2 = float(input('Nota 2: '))
nota3 = float(input('Nota 3: '))
nota4 = float(input('Nota 4: '))
media = (nota1 + nota2 + nota3 + nota4) / 4 # faz o cálculo da média utilizando os dados fornecidos pelo usuário

print(f'Média Final: {media:.1f}') # imprime as informações na tela