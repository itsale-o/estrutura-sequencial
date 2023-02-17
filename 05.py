# 5. Faça um Programa que converta metros para centímetros. Você pode pedir o comprimento em metros
# para o usuário (input).

m = float(input('Insira uma medida (em m): ')) # input --> pede a informação apara o usuário
cm = m * 100 # converte metros para centímetro

print(f'A medida equivale a {cm:.0f} cm') # imprime a informação na tela