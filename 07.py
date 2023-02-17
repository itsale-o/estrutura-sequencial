# 7. Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para
# o usuário

lado = float(input('Lado do quadrado: ')) # pede a informação para o usuário
area = lado ** 2 # ** é a função potência
dobro_area = area * 2

print(f'Área: {area:.2f}')
print(f'Dobro da área: {dobro_area:.2f}')