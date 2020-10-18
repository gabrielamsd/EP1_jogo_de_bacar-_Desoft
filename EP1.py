# n = índice das cartas para recuperar na lista
# append = aplica na lista os novos elementos
# regras da terceira carta para o banco implemetadas
# refinação do código para não ficar muito extenso
import random
# lista de cartas e lista de valores das cartas 
# add *8 pra ser oito baralho completo de 52 cartas - contador adicionado que limita o número de cartas para 4 por baralho, 32 cartas de cada símbolo.
def sorteio_de_cartas(cartas, contador, mão, n_cartas):
    i = 0
    while i< n_cartas: 
        índice_carta = random.randint(0,12)
        carta = cartas[índice_carta]
        if contador[n_cartas] > 0:
            mão.append(carta)
            contador[índice_carta] -= 1
            i += 1
        
    return mão
# add comissão para 8 baralhos
# implementando regras de valores para diferente
# s apostas
def comissão(aposta, valor_da_aposta, fichas):
    if aposta == 'B':
        fichas += valor_da_aposta * 0.9894 
    elif aposta == 'E':
        fichas += valor_da_aposta * 0.8564 * 8
    elif aposta == 'J':
        fichas += valor_da_aposta * 0.9876 * 0.95
    return fichas

aposta_vencedora = 0
# adicionando opções de jogo com 6 ou 8 baralhos.
inválido = True
while inválido:
    baralhos = int(input('Gostaria de jogar com 6 ou 8 baralhos? ' ))
    if baralhos != 6 and baralhos != 8:
        print('Quantidade de baralhos inválida. Opções possíveis: 6 ou 8')
    else:
        inválido = False

# adicionando opção de escolha no número de jogadores
número_de_jogadores = int(input('Quantos jogadores participarão? Digite apenas números por favor. '))
cartas = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'] 
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0, 0, 0]
fichas_iniciais = 100
fichas = [fichas_iniciais]  * número_de_jogadores

if baralhos == 8:
    contador = [32]*len(cartas)  # 32 cartas de cada pois em um baralho existem 4 naipes. com 8 baralhos o limite fica 32 cartas para cada símbolo
elif baralhos == 6:
    contador = [24]*len(cartas)  # 24 cartas de cada pois em um baralho existem 4 naipes. com 6 baralhos o limite fica 24 cartas para cada símbolo

# adicionando mais jogadores para apostar
# adicionado while e condição de validade para a interação
jogando = True
while jogando:
    jogador1 = [] # listas vazias para as cartas serem adicionadas
    banco = []
    apostas = [0] * número_de_jogadores # mudei essas listas porque quando um jogador perde ele deixa de apostar e ai o indice das listas ficam diferentes.
    valores_das_apostas = [0] * número_de_jogadores
    
    i = 0 
    while i < número_de_jogadores:
        if fichas[i] > 0: # se alguém perde as fichas, perde o jogo e para de poder apostar
            print('\nJogador {0}, você está começando a rodada com {1:.2f} fichas'.format(i+1, fichas[i]))
            inválido = True # invalida as situações em que o jogo não poderia acontecer. evita apostar mais do que poderia e escrever termos sem sentido
            while inválido:
                aposta = input('Qual é sua aposta? Digite "B" para banco, "E" para empate e "J" para jogador. '.format(i+1)) # padronização de apenas uma letra maiúscula para não dificultar a escrita
                if aposta != 'B' and aposta != 'E' and aposta != 'J':
                    print('Aposta inválida!')
                else:
                    inválido = False
                    apostas[i] = aposta
            inválido = True
            while inválido:    
                valor_da_aposta = int(input('Quanto você aposta? Digite apenas números por favor. '))
                if valor_da_aposta > fichas[i]:
                    print('Você não possui essa quantidade de fichas. Seu limite é {}'.format(fichas[i]))
                else:
                    valores_das_apostas[i] = valor_da_aposta
                    inválido = False
        i += 1


    # sorteando duas cartas para cada um
    # adicionado falar as cartas selecionadas para organizar a interação
    # adicionada a função para substituir o parágrafo
    print('\nSorteando...')
    jogador1 = sorteio_de_cartas(cartas, contador, jogador1, 2)
    banco = sorteio_de_cartas(cartas, contador, banco, 2)
    print('Cartas da jogador:', jogador1)
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
    print('Soma das cartas do jogador:', soma_das_cartas1)
    print('Soma das cartas do banco:', soma_das_cartasb)

    # condições:
    # quando a soma das cartas é inferior a 5 e 6... ocorre o sorteio de mais uma carta para o jogador 1 e a partir disso é avaliado se o banco receberá outra carta
    # ...nas duas somas: 
    sorteia_banco = False
    if soma_das_cartas1 <= 5 and soma_das_cartasb <= 6:
        jogador1 = sorteio_de_cartas(cartas, contador, jogador1, 1)
        soma_das_cartas1 += valores[cartas.index(jogador1[2])]

        if soma_das_cartas1 > 9:
            soma_das_cartas1 -= 10
        print('As somas das cartas do jogador e das cartas do banco foram ambas muito pequenas. Sorteando uma terceira carta para o jogador 1 e avaliando se o banco receberá mais uma carta...')
        print('Nova carta do jogador:', jogador1[2])
        print('Nova soma das cartas do jogador:', soma_das_cartas1)

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
        jogador1 = sorteio_de_cartas(cartas, contador, jogador1, 1) 
        soma_das_cartas1 += valores[cartas.index(jogador1[2])] 
        if soma_das_cartas1 > 9:
            soma_das_cartas1 -= 10 
        print('A soma das cartas do jogador foi menor que 5. Nova soma das cartas:', soma_das_cartas1)
    # ...na soma das cartas do banco:
    if soma_das_cartasb <= 5 and soma_das_cartas1 > 5 and soma_das_cartas1 < 8:
        sorteia_banco = True
        print('A soma das cartas do banco foi menor que 5')
        
    if sorteia_banco == True:
        banco = sorteio_de_cartas(cartas, contador, banco, 1) 
        soma_das_cartasb += valores[cartas.index(banco[2])]  
        if soma_das_cartasb > 9:
            soma_das_cartasb -= 10
        print('Nova carta do banco:', banco[2])
        print('Nova soma das cartas do banco:', soma_das_cartasb) 

    # adicionado vencer = True para facilitar e diminuir o programa
    # se o resultado for 6 e ou 7 nas somas são três possibilidades:
    # o banco vence,
    if soma_das_cartas1 == 6 and soma_das_cartasb == 7:
            aposta_vencedora = 'B'
    # o jogador vence, ou empate, que sera apresentado junto às outras opções de empate
    if soma_das_cartas1 == 7 and soma_das_cartasb == 6:
            aposta_vencedora = 'J'

    # condições para vencer com 8 ou 9:
    if (soma_das_cartas1 == 8 or soma_das_cartas1 == 9) and (soma_das_cartasb != 8 and soma_das_cartasb != 9):
            aposta_vencedora = 'J'
    if (soma_das_cartasb == 8 or soma_das_cartasb == 9) and (soma_das_cartas1 != 8 and soma_das_cartas1 != 9):
            aposta_vencedora = 'B'
    # empates aqui
    if (soma_das_cartasb == 8 or soma_das_cartasb == 9) and (soma_das_cartas1 == 8 or soma_das_cartas1 == 9) or ((soma_das_cartas1 == 6 and soma_das_cartasb == 6) or (soma_das_cartas1 == 7 and soma_das_cartasb == 7)):
            aposta_vencedora = 'E'
    # quando a terceira carta já foi sorteada mas ainda não são 8 ou 9:
    else: 
        if soma_das_cartasb > soma_das_cartas1:
                aposta_vencedora = 'B'
        if soma_das_cartas1 > soma_das_cartasb:
                aposta_vencedora = 'J'
        if soma_das_cartasb == soma_das_cartas1:
                aposta_vencedora = 'E'

    print('\nA aposta vencedora foi: {}'.format(aposta_vencedora))
    i=0 
    while i < número_de_jogadores:
        if fichas[i] > 0:
            if apostas[i] == aposta_vencedora:
                fichas[i] = comissão(apostas[i], valores_das_apostas[i], fichas[i])
                print('\nJogador {}, você ganhou essa rodada!'.format(i+1))
                print('Você tem {0:.2f} fichas'.format(fichas[i])) # conversei com o andrew sobre o número de casas decimais e ele disse que uma boa ideia seria reduzir pra duas 
            elif apostas[i] != aposta_vencedora:
                fichas[i] -= valores_das_apostas[i]
                print('\nJogador {},você perdeu sua aposta'.format(i+1))
                print('Você tem {0:.2f} fichas'.format(fichas[i]))
        i += 1
 # quem decidir sair do jogo no meio tem suas fichas zeradas, deixando os outros jogadores dando continuidade
    i = 0
    while i < número_de_jogadores:
        if fichas[i] > 0:
            jogar_novamente = input('\nJogador {}, deseja continuar jogando? Digite "C" para continuar ou "S" para sair do jogo: '.format(i+1))
            if jogar_novamente == "S":
                fichas[i] = -1 # Com as fichas em um valor negativo, ele sai da condição, se não, toda rodada iria avisar que ele saiu.
                print('Obrigado por jogar!')
        elif fichas[i] == 0:
            print('\nJogador {}, você perdeu o jogo por falta de fichas. '.format(i+1))
            continuar_jogando = input('Deseja continuar jogando? Se sim, digite "C", caso contrário digita qualquer outra tecla. ')
            if continuar_jogando == "C":
                fichas2 = input("Quantas fichas deseja comprar? Digite apenas números, por favor. ")
                fichas[i] = fichas2
            else:
                print('obrigado por jogar!')
                fichas[i] = -1 # Com as fichas em um valor negativo, ele sai da condição, se não, toda rodada iria avisar que ele perdeu.
        i += 1    

        
    # se alguém quiser entrar no meio, os jogadores continuam com o numero de fichas que tinham e esse novo jogador passa a participar com o valor inicial de fichas
    acrescenta_jogadores = input('\nDeseja acrescentar jogadores na partida? "S" para sim e "N" para não. ')
    if acrescenta_jogadores == "S":
        recrutas = int(input('Quantos jogadores deseja acrescentar? '))
        número_de_jogadores += recrutas
        i = 0
        while i < recrutas:
            fichas.append(fichas_iniciais)
            i +=1
