EP1_jogo_de_bacara_Desoft

Esse repositório é um jogo de bacará desenvolvido em python.

Produzido por Gabriela Duarte no primeiro semestre de engenharia na instituição Insper.

Primeira versão - dia 24/09/2020, Versão final - dia 18/10/2020

O jogo funciona da seguinte forma:

O jogo começa com a escolha da quntidade de baralhos (1, 6 ou 8) e a escolha da quantidade de jogadores que participarão. Os jogadores realizam suas apostas colocando a quantidade de fichas que quiserer (limitado pela quantidade de fichas que o jogador possui naquele momento) em quem acredita ser o vencedor (jogador, banco ou empate). A partir desse momento a mesa realiza todo o restante do jogo automaticamente.

Inicialmente a mesa embaralha as cartas e distribui duas para uma mão e duas para o banco. Se a soma das cartas do jogador ou do banco for igual a 8 ou 9 o jogo termina e as apostas são pagas. Se a soma das cartas tanto do jogador quanto do banco forem diferentes de 8 ou 9, a mesa decide se distribuirá uma terceira carta a cada um de acordo com as algumas regras, começando pelo jogador e depois distribuindo a carta do banco:

Se a soma das cartas for 6 ou 7, não distribui mais uma carta, vence quem tiver a carta maior.

Se a soma das cartas for 5 ou menos, distribui mais uma carta e a soma é recalculada.

Importante: se a soma das cartas  for >= 10, conta apenas o valor da unidade. As cartas numéricas têm o valor respectivo ao número, enquanto As vale 1 e as outras (J, Q e K) valem 0.

Se a soma de um deles é menor que 6, mas a do outro é maior, só o que teve o valor menor ganha a terceira carta. Se os dois tem a soma das cartas inferior a 6, a mão recebe uma terceira carta e, dependendo da soma das cartas do banco e da nova carta da mão, o banco recebe ou não uma terceira carta. Essa combinação de cartas anteriores-carta nova da mão é apresentado por uma tabela e implementada automaticamente pelo jogo.

Em cassinos é comum existir uma comissão sobre as apostas recebidas no Bacará. Se o jogador perde a aposta ele não paga nada de comissão nessa partida. Entretanto, se ele ganha a aposta, é necessário pagar uma porcentagem do que ele for receber para a casa, já implementada no jogo.

Caso o ganhador acerte a aposta, além da comissão existe outra regra para o recebimento de fichas: 

- Se o jogador venceu a partida (obteve a soma mais próxima de 9), a mesa paga a mesma quantidade de fichas apostadas para os jogadores que apostaram nele.
- Se o banco venceu a partida, a mesa paga 95% das fichas apostadas para quem apostou nele.
- Se ocorrer um empate, e algum jogador apostou no empate, a mesa paga 8 vezes a quantidade de fichas apostadas por ele.
