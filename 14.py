# 14. João Papo-de-Pescador, homem de bem comprou um microcomputador para controlar o rendimento
# diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o establecido pelo
# regulamento de pesca do estado de São Paulo (50 kg) deve pagar uma multa de R$ 4,00 por quilo
# excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e
# calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável
# multa o valor da multa que João devrá pagar. Imprima com as mensagens adequadas.

peso = float(input('Peso de peixes (em kg): ')) # pede a informação para o usuário

if peso <= 50: # if --> caso o peso do peixe não exceda a condição dada pelo exercício
    print('Não houve excesso de peso portanto não haverá multa') # imprime a mensagem
else: # else --> caso a condição acima não seja verdadeira, executa o código abaixo
    excesso = peso - 50 # calcula o excesso de peso
    multa = excesso * 4 # calcula a multa a ser aplciada
    print(f'Peso de peixes: {peso:.2f} kg\nExcesso: {excesso:.2f} kg\nMulta a pagar: R$ {multa:.2f}')
    # imprime as informações