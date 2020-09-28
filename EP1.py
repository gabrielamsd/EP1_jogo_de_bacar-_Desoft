# n = índice das cartas para recuperar na lista
# append = aplica na lista os novos elementos
# regras da terceira carta para o banco implemetadas
import random
# lista de cartas e lista de valores das cartas 
# add *4 pra ser um baralho completo de 52 cartas
cartas = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] * 4
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
fichas1 = 100
# por enquanto só um jogador e o banco
# adicionado while e condição de validade para a interação
jogando = True
while jogando:
    venceu = True
    jogador1 = []
    banco = []
    print('Você está começando a rodada com {} fichas'.format(fichas1))
    inválido = True
    while inválido:
        aposta = input('Qual é sua aposta? Digite "B" para banco, "E" para empate e "J" para jogador. Para sair do jogo aperte S. ') 
        if aposta != 'B' and aposta != 'E' and aposta != 'J':
            print('Aposta inválida!')
        elif aposta == 'S':
            jogando = False
        else:
            inválido = False
    inválido = True
    while inválido:    
        valor_da_aposta = int(input('Quanto você aposta? '))
        if valor_da_aposta > fichas1:
            print('Você não possui essa quantidade de fichas. Seu limite é {}'.format(fichas1))
        else:
            inválido = False

    # adicionado falar as cartas selecionadas para organizar a interação
    i = 0
    while i < 2:
        n_jogador1 = random.randint(0,12)
        n_banco = random.randint(0,12)
        carta_jogador1 = cartas[n_jogador1]
        carta_banco = cartas[n_banco]
        jogador1.append(carta_jogador1)
        banco.append(carta_banco)
        i += 1
    print('Suas cartas:', jogador1)
    print('Cartas do banco:', banco)
    
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
    # quando a soma das cartas é inferior a 5 e 6... ocorre o sorteio de mais uma carta para o jogador 1 e a partir disso é avaliado se o banco receberá outra carta
    # ...nas duas somas: 
    sorteia_banco = False
    if soma_das_cartas1 <= 5 and soma_das_cartasb <= 6:
        n_jogador1 = random.randint(0,12)
        carta_jogador1 = cartas[n_jogador1]
        jogador1.append(carta_jogador1)
        índice_valor1 = cartas.index(jogador1[2])
        soma_das_cartas1 += valores[índice_valor1]
        if soma_das_cartas1 > 9:
            soma_das_cartas1 -= 10
        print('As somas das suas cartas e das cartas do banco foram ambas muito pequenas. Sorteando uma terceira carta para o jogador 1 e avaliando se o banco receberá mais uma carta...')
        print('Sua nova carta:', jogador1[2])
        print('Nova soma das suas cartas:', soma_das_cartas1)

        if (soma_das_cartasb == 6) and (valores[cartas.index(jogador1[2])] == 6 or valores[cartas.index(jogador1[2])] == 7):
            sorteia_banco = True
        elif (valores[cartas.index(jogador1[2])] > 3 and valores[cartas.index(jogador1[2])] < 8) and soma_das_cartasb == 5:
            sorteia_banco = True
        elif valores[cartas.index(jogador1[2])] == 4 and soma_das_cartasb > 1 and soma_das_cartasb < 8:
            sorteia_banco = True
        elif soma_das_cartasb == 3 and valores[cartas.index(jogador1[2])] != 8:
            sorteia_banco = True
        elif valores[cartas.index(jogador1[2])] >= 0 and soma_das_cartasb < 3:
            sorteia_banco = True
        else:
            sorteia_banco = False  
            print('O banco não recebe outra carta') 
      
    # ...na soma das cartas jogador1:
    if soma_das_cartas1 <= 5 and (soma_das_cartasb >= 6 and soma_das_cartasb <= 7):
        n_jogador1 = random.randint(0,12)
        carta_jogador1 = cartas[n_jogador1]
        jogador1.append(carta_jogador1)
        índice_valor1 = cartas.index(jogador1[2])
        soma_das_cartas1 += valores[índice_valor1]  
        if soma_das_cartas1 > 9:
            soma_das_cartas1 -= 10 
        print('A soma das suas cartas foi menor que 5. Nova soma das cartas:', soma_das_cartas1)
    # ...na soma das cartas do banco:
    if soma_das_cartasb <= 5 and soma_das_cartas1 > 5 and soma_das_cartas1 < 8:
        sorteia_banco = True
        print('A soma das cartas do banco foi menor que 5')
        
    if sorteia_banco == True:
        n_banco = random.randint(0,12)
        carta_banco = cartas[n_banco]
        banco.append(carta_banco)
        índice_valorb = cartas.index(banco[2])
        soma_das_cartasb += valores[índice_valorb]   
        if soma_das_cartasb > 9:
            soma_das_cartasb -= 10
        if soma_das_cartas1 > 9:
            soma_das_cartas1 -= 10 
        print('Nova soma das cartas do banco:', soma_das_cartasb) 

    # adicionado vencer = True para facilitar e diminuir o programa
    # se o resultado for 6 e ou 7 nas somas são três possibilidades:
    # o banco vence,
    if soma_das_cartas1 == 6 and soma_das_cartasb == 7:
        if aposta == 'B':
            venceu = True
        elif aposta == 'E':
           venceu = False
        elif aposta == 'J':
            venceu = False
    # o jogador vence, ou empate, que sera apresentado junto às outras opções de empate
    if soma_das_cartas1 == 7 and soma_das_cartasb == 6:
        if aposta == 'B':
           venceu = False
        elif aposta == 'E':
            venceu = False
        elif aposta == 'J':
            venceu = True 

    # condições para vencer com 8 ou 9:
    if (soma_das_cartas1 == 8 or soma_das_cartas1 == 9) and (soma_das_cartasb != 8 and soma_das_cartasb != 9):
        if aposta == 'B':
            venceu = False
        elif aposta == 'E':
            venceu = False
        elif aposta == 'J':
            venceu = True
    if (soma_das_cartasb == 8 or soma_das_cartasb == 9) and (soma_das_cartas1 != 8 and soma_das_cartas1 != 9):
        if aposta == 'B':
            venceu = True
        elif aposta == 'E':
           venceu = False
        elif aposta == 'J':
            venceu = False
    # empates aqui!!!
    if (soma_das_cartasb == 8 or soma_das_cartasb == 9) and (soma_das_cartas1 == 8 or soma_das_cartas1 == 9) or ((soma_das_cartas1 == 6 and soma_das_cartasb == 6) or (soma_das_cartas1 == 7 and soma_das_cartasb == 7)):
        if aposta == 'B':
           venceu = False
        elif aposta == 'E':
            venceu = True
        elif aposta == 'J':
            venceu = False
    # quando a terceira carta já foi sorteada mas ainda não são 8 ou 9:
    else: 
        if soma_das_cartasb > soma_das_cartas1:
            if aposta == 'B':
                venceu = True
            elif aposta == 'E':
                venceu = False
            elif aposta == 'J':
               venceu = False
        if soma_das_cartas1 > soma_das_cartasb:
            if aposta == 'B':
                venceu = False
            elif aposta == 'E':
                venceu = False
            elif aposta == 'J':
                venceu = True
        if soma_das_cartasb == soma_das_cartas1:
            if aposta == 'B':
                venceu = False
            elif aposta == 'E':
                venceu = True
            elif aposta == 'J':
                venceu = False

    if venceu == True:
        fichas1 += valor_da_aposta
        print('Você ganhou essa rodada')
        print('Você tem {} fichas'.format(fichas1))

    elif venceu == False:
        fichas1 -= valor_da_aposta
        print('Você perdeu sua aposta')
        print('Você tem {} fichas'.format(fichas1))
    # para finalizar o loop:
    if fichas1 <= 0:
        jogando = False
        print('Você perdeu o jogo.')