# n = índice das cartas para recuperar na lista
# append = aplica na lista os novos elementos
# transformar empate em função
import random
# lista de cartas e lista de valores das cartas 
cartas = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
fichas1 = 100
# por enquanto só um jogador e o banco
jogador1 = []
banco = []
print('Você está começando a rodada com {} fichas'.format(fichas1))
aposta = input('Qual é sua aposta? Digite "B" para banco, "E" para empate e "J" para jogador. Para sair do jogo aperte S. ') 
valor_da_aposta = int(input('Quanto você aposta? '))
# sortear as cartas e colocar elas sorteadas na lista vazia do jogador e do banco
i = 0
while i < 2:
    n_jogador1 = random.randint(0,12)
    n_banco = random.randint(0,12)
    carta_jogador1 = cartas[n_jogador1]
    carta_banco = cartas[n_banco]
    jogador1.append(carta_jogador1)
    banco.append(carta_banco)
    i += 1
print(jogador1)
print(banco)
# atribuir o valor da lista "valores" às cartas da lista "cartas" e somar as sorteadas anteriormente
i = 0
soma_das_cartas1 = 0
soma_das_cartasb =  0
while i < 2:
    índice_valor1 = cartas.index(jogador1[i])
    índice_valorb = cartas.index(banco[i])
    soma_das_cartas1 += valores[índice_valor1]
    soma_das_cartasb += valores[índice_valorb]
    i += 1
# quando a soma é superior a 9, a unidade é o resultado da soma, assim, se maior que 9, deve ser subitraído 10 do total
if soma_das_cartas1 > 9:
    soma_das_cartas1 -= 10
if soma_das_cartasb > 9:
    soma_das_cartasb -= 10
print('Soma das suas cartas:', soma_das_cartas1)
print('Soma das cartas do banco:', soma_das_cartasb)

# condições:
# quando a soma das cartas é inferior a 5... ocorre o sorteio de mais uma carta para aquele(s) que teve(tiveram) a soma menor que 5
# ...nas duas somas: 
if soma_das_cartas1 <= 5 and soma_das_cartasb <= 5:
    n_jogador1 = random.randint(0,12)
    n_banco = random.randint(0,12)
    carta_jogador1 = cartas[n_jogador1]
    carta_banco = cartas[n_banco]
    jogador1.append(carta_jogador1)
    banco.append(carta_banco)
    índice_valor1 = cartas.index(jogador1[2])
    índice_valorb = cartas.index(banco[2])
    soma_das_cartas1 += valores[índice_valor1]
    soma_das_cartasb += valores[índice_valorb]
    if soma_das_cartas1 > 9:
        soma_das_cartas1 -= 10
    if soma_das_cartasb > 9:
        soma_das_cartasb -= 10
    print('As duas somas das cartas foram menores que 5. Sorteando uma terceira carta...')
    print('Nova soma das suas cartas:', soma_das_cartas1)
    print('Nova soma das cartas do banco:', soma_das_cartasb)  
# ...na soma das cartas jogador1:
elif soma_das_cartas1 <= 5 and soma_das_cartasb > 5:
    n_jogador1 = random.randint(0,12)
    carta_jogador1 = cartas[n_jogador1]
    jogador1.append(carta_jogador1)
    índice_valor1 = cartas.index(jogador1[2])
    soma_das_cartas1 += valores[índice_valor1]
    if soma_das_cartas1 > 9:
        soma_das_cartas1 -= 10  
        print('A soma das suas cartas foram menores que 5. Nova soma das cartas:', soma_das_cartas1)
# ...na soma das cartas do banco:
elif soma_das_cartasb <= 5 and soma_das_cartas1 > 5:
    n_banco = random.randint(0,12)
    carta_banco = cartas[n_banco]
    banco.append(carta_banco)
    índice_valorb = cartas.index(banco[2])
    soma_das_cartasb += valores[índice_valorb]
    if soma_das_cartasb > 9:
        soma_das_cartasb -= 10 
    print('A soma das cartas do banco foram menores que 5. Nova soma das cartas:', soma_das_cartasb)  
# se o resultado for 6 e ou 7 nas somas são três possibilidades:
# o banco vence,
if soma_das_cartas1 == 6 and soma_das_cartasb == 7:
    if aposta == 'B':
        fichas1 += valor_da_aposta
        print('Você ganhou essa rodada')
        print('Você tem {} fichas'.format(fichas1))
    elif aposta == 'E':
        fichas1 -= valor_da_aposta
        print('Você perdeu sua aposta')
        print('Você tem {} fichas'.format(fichas1))
    elif aposta == 'J':
        fichas1 -= valor_da_aposta
        print('Você perdeu sua aposta')
        print('Você tem {} fichas'.format(fichas1))
# o jogador vence, ou empate, que sera apresentado junto às outras opções de empate.
if soma_das_cartas1 == 7 and soma_das_cartasb == 6:
    if aposta == 'B':
        fichas1 -= valor_da_aposta
        print('Você perdeu sua aposta')
        print('Você tem {} fichas'.format(fichas1))
    elif aposta == 'E':
        fichas1 -= valor_da_aposta
        print('Você perdeu sua aposta')
        print('Você tem {} fichas'.format(fichas1))
    elif aposta == 'J':
        fichas1 += valor_da_aposta
        print('Você ganhou essa rodada')
        print('Você tem {} fichas'.format(fichas1))

# condições para vencer com 8 ou 9:
if (soma_das_cartas1 == 8 or soma_das_cartas1 == 9) and (soma_das_cartasb != 8 and soma_das_cartasb != 9):
    if aposta == 'B':
        fichas1 -= valor_da_aposta
        print('Você perdeu sua aposta')
        print('Você tem {} fichas'.format(fichas1))
    elif aposta == 'E':
        fichas1 -= valor_da_aposta
        print('Você perdeu sua aposta')
        print('Você tem {} fichas'.format(fichas1))
    elif aposta == 'J':
        fichas1 += valor_da_aposta
        print('Você ganhou essa rodada')
        print('Você tem {} fichas'.format(fichas1))
if (soma_das_cartasb == 8 or soma_das_cartasb == 9) and (soma_das_cartas1 != 8 and soma_das_cartas1 != 9):
    if aposta == 'B':
        fichas1 += valor_da_aposta
        print('Você ganhou essa rodada')
        print('Você tem {} fichas'.format(fichas1))
    elif aposta == 'E':
        fichas1 -= valor_da_aposta
        print('Você perdeu sua aposta')
        print('Você tem {} fichas'.format(fichas1))
    elif aposta == 'J':
        fichas1 -= valor_da_aposta
        print('Você perdeu sua aposta')
        print('Você tem {} fichas'.format(fichas1))
# empates aqui!!!
if (soma_das_cartasb == 8 or soma_das_cartasb == 9) and (soma_das_cartas1 == 8 or soma_das_cartas1 == 9) or ((soma_das_cartas1 == 6 and soma_das_cartasb == 6) or (soma_das_cartas1 == 7 and soma_das_cartasb == 7)):
    if aposta == 'B':
        fichas1 -= valor_da_aposta
        print('Você perdeu sua aposta')
        print('Você tem {} fichas'.format(fichas1))
    elif aposta == 'E':
        fichas1 += valor_da_aposta
        print('Você ganhou essa rodada')
        print('Você tem {} fichas'.format(fichas1))
    elif aposta == 'J':
        fichas1 -= valor_da_aposta
        print('Você perdeu sua aposta')
        print('Você tem {} fichas'.format(fichas1))
# quando a terceira carta já foi sorteada mas ainda não são 8 ou 9:
else: 
    if soma_das_cartasb > soma_das_cartas1:
        if aposta == 'B':
            fichas1 += valor_da_aposta
            print('Você ganhou essa rodada')
            print('Você tem {} fichas'.format(fichas1))
        elif aposta == 'E':
            fichas1 -= valor_da_aposta
            print('Você perdeu sua aposta')
            print('Você tem {} fichas'.format(fichas1))
        elif aposta == 'J':
            fichas1 -= valor_da_aposta
            print('Você perdeu sua aposta')
            print('Você tem {} fichas'.format(fichas1))
    if soma_das_cartas1 > soma_das_cartasb:
        if aposta == 'B':
            fichas1 -= valor_da_aposta
            print('Você perdeu sua aposta')
            print('Você tem {} fichas'.format(fichas1))
        elif aposta == 'E':
            fichas1 -= valor_da_aposta
            print('Você perdeu sua aposta')
            print('Você tem {} fichas'.format(fichas1))
        elif aposta == 'J':
            fichas1 += valor_da_aposta
            print('Você ganhou essa rodada')
            print('Você tem {} fichas'.format(fichas1))
    if soma_das_cartasb == soma_das_cartas1:
        if aposta == 'B':
            fichas1 -= valor_da_aposta
            print('Você perdeu sua aposta')
            print('Você tem {} fichas'.format(fichas1))
        elif aposta == 'E':
            fichas1 += valor_da_aposta
            print('Você ganhou essa rodada')
            print('Você tem {} fichas'.format(fichas1))
        elif aposta == 'J':
            fichas1 -= valor_da_aposta
            print('Você perdeu sua aposta')
            print('Você tem {} fichas'.format(fichas1))