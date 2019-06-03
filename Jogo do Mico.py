#importando as bibliotecas
import time
import random
import FuncoesJM
Novamente = True
while Novamente: #Aqui controlo no final do jogo se o usuario quer jogar novamente
    print ("\n"*40)
    print ('Bem vindo ao Jogo Do Mico\n')
    print ('Menu:\n')
    print ('1. Instruções:')
    print ('2. Começar:')
    print ('3. Sair:')
    comando = '' #Para força a entrada no while a seguir
    while comando != '2' and comando != '3':   #Forço a entrada com o comando diferente de uma das duas instruções


        if comando != '1':
            comando = input("Digite um dos numeros do menu: ")  #Pedi para introduzir um numero do menu


            while not FuncoesJM.validar(comando,['1','2','3']):   #Aqui uso a função validar para saber se o usuario digitou as opções do menu
                print ('Não temos a opção "%s" no menu.\ntente novamente.'%comando)  #Mensagem informando que a opção está indisponível
                comando = input("Digite um dos numero do menu: ")  #Peço para digitar novamente


        if comando == '1':      #Se o comando for 1, exibo as instruções do jogo
            print('\nInstrições:')
            print('\n   O jogo do mico é formado por um baralho de 40 cartas de animais,\n20 desses animais são fêmeas e os outros 20 são machos,\nexistem 10 nomes de animais diferentes neste baralho.')
            print('   O objetivo do jogo é formar pares de animais com o mesmo nome e sexo diferente.')
            print('   Cada jogador recebe um total de 6 cartas.')
            print('   Para pegar as novas cartas digite "sim" ou "não".')
            print('   Cada jogador após a 1º jogada pode pegar a carta que seu adversário descartou ou puxar uma nova carta.')
            print('   O jogo acaba  quando um dos jogadores fizerem 3 pares e esse jogador sera o vencedor.')
            print('   A qualquer momento dentro do jogo, você pode desistir do jogo,\nbasta digitar "/surrender" e você dara a vitoria para seu adversário.\n')
            print ('2. Começar:')
            print ('3. Sair:')
            comando = input("Digite um dos numeros do menu: ")   #Assim que termino de exibir as instruções peço para me informar outra opção


            while not FuncoesJM.validar(comando,['1','2','3']):    #Vejo se digitou os numeros do menu
                print ('Não existe a opção "%s" no menu.\nTente novamente.'%comando)   #Mensagem informando que a opção não está disponível 
                comando = input('Digite um dos numero do menu: ')  #Peço para introduzir um novo comando


    if comando == '3':
        Parar = True   #O usuario decidiu fechar o jogo e a variavel "Parar" é responsavel para não executar o jogo no assim que iniciado
        print("Você fechou o jogo!")  #Mensagem informando que pediram para fechar o jogo
        Novamente = False
    #Variaveis que precisarei no jogo e criação do baralho

    aceitar = ["vou","sim", "yes", "y", "s", "não", "nao", "no", "not", "n","/surrender"]   #Unicos comandos que eu aceito como ordem do meu usuario
    Animais = ["Cobra", "Elefante", "Girafa", "Hétero", "Morcego", "Sapo", "Pavão", "Peixe", "Taniby", "Unicórnio"]    #Nome dos Animais
    BaralhoF = []               #Baralho Femea Vazio
    BaralhoM = []                #Baralho Macho Vazio
    Descartadas = []             #Baralho das cartas que serão descartadas durante o jogo
    Jogada = aceitar[0]          #Preciso que essa variavel ja tenha sido definida para não dar erro durante a rendição ou o fechamento do jogo
    Descartar = aceitar[0]          #Preciso que essa variavel ja tenha sido definida para não dar erro durante a rendição ou o fechamento do jogo

    for x in range(2):                                                                                          # Duplicar os baralhos

        for x in range(len(Animais)):                                                                       # Criando os Baralhos com nome dos animais e sexo com a quantidade de elementos/animais da lista "Animais"
            BaralhoF.extend([[Animais[x], "Fêmea"]])                                                 # Uso o modo "extend" para fazer com que os elementos das listas não tenham a mesma """"""referencia""""""""
            BaralhoM.extend([[Animais[x],"Macho"]])                                                 # o nome da lista "Animais" seguido do indice [x] para adcionar aos baralhos o animal de cada indice por vez

    BaralhoG = BaralhoF + BaralhoM                                                                      # Junto os dois baralhos em um baralho geral
    Ganhou = False                              #Preciso que essa variavel ja tenha sido definida para não dar erro durante a rendição ou o fechamento do jogo
    empate = False                              #Preciso que essa variavel ja tenha sido definida para não dar erro durante a rendição ou o fechamento do jogo
    Decidir = aceitar[0]

    #Aqui começa o Jogo no traçar dos baralhos

    print("\n"*42)
    if comando != '3':       #Diferente do comando "3" para iniciar o jogo indicando
        print("O Jogo vai começar em:")             #print exibindo que o jogo vai começar


        for x in range(1,4):                        # esse for é para contagem regressiva antes do inicio do jogo
            print (4-x,"."*(4-x))
            time.sleep(1)
        Parar = False                       #Preciso dessa variavel já definida para não causar erro durante algumas comparações
        print ("\n"* 41)
        print ("Bom Jogo\n")
        print ("Insira o nome dos jogadores")
        Jogador1 = input("Nome do 1º Jogador(a): ")                                        # Recebendo o nome do 1º jogador
        Jogador2 = input("Nome do 2º Jogador(a): ")                                        # Recebendo o nome do 2º jogador
        print("\n"*41)
        NumCartas = 6                                                                                               # Numero de cartas de cada jogador
        CartasJogador1 = []                                                                                     # Mão vazia do 1º Jogador
        CartasJogador2 = []                                                                                     # Mão vazia do 2º Jogador
        print("\nEmbaralhando as cartas...")
        time.sleep(1.5)
        print("\n"*41)
        random.shuffle(BaralhoG)                                                                                # Misturo os elementos/cartas chamando a função "shuffle"
        print("\nDistribuindo as cartas para os Jogadores %s e %s...\n"%(Jogador1,Jogador2))
        time.sleep(2)
        print("\n"*41)


        for x in range(NumCartas):                                                                          # Distribuição das Cartas
            CartasJogador1 += [BaralhoG.pop(len(BaralhoG)-1)]                               # Usando a quantidade de elementos do baralho geral - 1 para obter o indice do ultimo elemento da lista/Baralho
            CartasJogador2 += [BaralhoG.pop(len(BaralhoG)-1)]


        if FuncoesJM.vence(CartasJogador1):
            print("Jogador(a) %s ganhou o jogo no inicio"% (Jogador1))
            Parar = True                                                                                                            #Ajeitar para caso aja a possibilidade dos 2 ganharem na primeira jogada


        if FuncoesJM.vence(CartasJogador2):
            print("Jogador(a) %s ganhou o jogo no inicio"% (Jogador2))
            Parar = True
        NumJogada = 1                                                                                           # Essa variavel guarda o numero da jogada atual


    while (len(BaralhoG) != 0) and (not Parar):                                                                           # Quando a quantidade de cartas do Baralho acabar o jogo termina ou condição de termino do jogo
        
        PegouDescarte = False


        if NumJogada %2 != 0:                                                                           # Aqui eu controlo quem é a vez de jogar, dividindo o numero da jogada atual pela quantidade de jogadores
            JogadorVez = Jogador1                                                                  # Esta variavel me indica quem é o jogador da vez
            Mão = CartasJogador1                                    #Altero a mão da vez para as cartas do jogador da vez
            OutroJogador = Jogador2                                 #Para saber qual opnente fez tal movimento


        else:
            JogadorVez = Jogador2           #Mesmo procedimento do "if" só que para jogadas pares ou seja do 2º jogador
            Mão = CartasJogador2
            OutroJogador = Jogador1


        if (NumJogada > 1):                 #Para não exibir as cartas do adversario depois da primeira rodada
            print("\n"*43)
        print("Vez do jogador(a) %s\n"%JogadorVez)                                                      # Print para exibit o nome do jogador da vez


        if (NumJogada > 1):
            time.sleep(3)
            print("\n"*43)
        print("{0:^66}".format("Jogada de nº%d"%NumJogada))                                               # Print para exibir o numero da jogada atual
        time.sleep(1)
        print("{0:^66}".format("Mão do jogador(a) %s"%JogadorVez))                                            #Print para introdução da mão do jogador da vez
        time.sleep(1)

        FuncoesJM.exibirCartas(Mão) #Função que criei para exibir as cartas com uma clareza e jogabilidade melhor
        FuncoesJM.quantPar(Mão)
        time.sleep(1)

        if NumJogada > 1 and not Ganhou:
            print("\n{0:^66}\n{1:^66}\n{2:^66}\n{1:^66}\n".format(("Esta carta foi descartada."),("#"*25),("#{0:^11}/{1:^11}#".format((Descartadas[len(Descartadas)-1][0]),(Descartadas[len(Descartadas)-1][1])))))   #Exibe a carta do topo da pilha de descartes
            Jogada = input("%s, vai querer a carta %s %s descartada pelo jogador %s? "%(JogadorVez, Descartadas[len(Descartadas)-1][0], Descartadas[len(Descartadas)-1][1],OutroJogador))   #Pergunta se o jogador da vez vai querer a carta que o jogador anterior mandou para o baralho de descartes
            time.sleep(1)


            while not FuncoesJM.validar(Jogada,aceitar) and Jogada != aceitar[10]:  #Vejo se ele digitou apenas o que eu permito e tambem não tenha desistido da partida
                print('Jogada "%s" inválida, por favor, tente novamente!'%Jogada)   #Caso tenha digitado algo que não seja aceitavel exibo essa msg e peço para digitar novamente
                Jogada = input("%s, vai querer a carta %s %s descartada pelo jogador %s? "%(JogadorVez, Descartadas[len(Descartadas)-1][0], Descartadas[len(Descartadas)-1][1],OutroJogador))

            if FuncoesJM.validar(str.lower(Jogada), aceitar[:5]) and Jogada != aceitar[10]:
                print("Para discartar digite o numero da carta que está na sua mão.") #Instruções para o usuario
                Mão.append(Descartadas.pop(len(Descartadas)-1)) #Já adiciono a carta a mão para que caso o jogador pegue a carta e depois não queira mais, basta apenas descarta-la e ainda poderar puxar uma nova
                Descartar = input("Qual carta deseja descartar da sua mão? ")

                while (not FuncoesJM.validar(Descartar,list(range(1,len(Mão)+1)))) and Descartar != aceitar[10]:  #Aqui peguei o numero de cartas que tem na mão, transformei em uma lista para que possa funcionar na função que criei
                    print ('A carta "%s" não existe.'%Descartar)
                    Descartar = input("Qual carta deseja descartar da sua mão? ")


                if int(Descartar) == (len(Mão)): #Condição para saber se ele realmente quis a carta, ou se arrependeu de pegar e quer pegar a proxima
                    PegouDescarte = False
                    print("%s, você descartou a carta de nº%s : %s %s"%(JogadorVez,Descartar,Mão[int(Descartar)-1][0],Mão[int(Descartar)-1][1]))
                    print("Que já estava descartada.")
                    print("Puxando a nova carta!")
                    time.sleep(0.5)
                    Descartadas.append(Mão.pop(int(Descartar)-1))


                       #Só chegara até aqui valores aceitaveis nos indices das cartas
                elif Descartar != aceitar[10]: #Vejo se ele não desistiu e então exibo a carta que ele descartou e se ele pegou a carta descartada
                    PegouDescarte = True
                    print("%s, você descartou a carta de nº%s : %s %s"%(JogadorVez,Descartar,Mão[int(Descartar)-1][0],Mão[int(Descartar)-1][1]))
                    Descartadas.append(Mão.pop(int(Descartar)-1))
                    Ganhou = FuncoesJM.vence(Mão) #Aqui verifico se o conjunto de cartas do jogador está com as condições de vitorias assim que ele alterou seu baralho e guardo esse valor logico em uma variavel
                    time.sleep(2)
            elif str.lower(Jogada) != aceitar[10]: #O perigo que vou fazer é aqui socorro gzus
                print("Você não quis a carta %s %s"%(Descartadas[len(Descartadas)-1][0],Descartadas[len(Descartadas)-1][1])) #Mensagem informando a carta que o jogador não quis


        if not PegouDescarte and Jogada != aceitar [10] and Descartar != aceitar[10] and not Ganhou: #Condições para verificar se o jogador desistiu em algum momento ou se ele pegou uma carta nova ou até mesmo ganhou o jogo

            
            NovaCarta = [BaralhoG.pop(len(BaralhoG)-1)] #Aqui eu puxo a nova carta do baralho, a que está no top do deck
            time.sleep(1)
            print("\n{0:^66}\n{1:^66}\n{2:^66}\n{1:^66}\n".format(("A nova carta de Nº%d é: "%(len(Mão)+1)),("#"*25),("#{0:^11}/{1:^11}#".format((NovaCarta[0][0]),(NovaCarta[0][1])))))   #Exibe a carta do topo da pilha de descartes
            time.sleep(1)
            Jogada = input("%s, vai querer a carta %s %s? "%(JogadorVez, NovaCarta[0][0], NovaCarta[0][1]))                                 # Pergunta se vai querer a nova carta e diz o nome dela


            while not FuncoesJM.validar(Jogada,aceitar): #Aqui eu nego o valor logico da função que me retorna True, fazendo com que se a jogada estiver nos parametros que eu defini para meu jogo aceitar não entrara aqui
                print('Jogada "%s" inválida, por favor, tente novamente!'%Jogada) #Mensagem informando que o usuario digitou uma jogada invalida
                Jogada = input("%s, vai querer a carta %s %s? "%(JogadorVez, NovaCarta[0][0], NovaCarta[0][1])) #Pergunto novamente se ele vai querer a carta


            if FuncoesJM.validar(str.lower(Jogada), aceitar[:5]):
                print("Para discartar digite o numero da carta que está na sua mão.")
                Mão.append(NovaCarta.pop())    #Aqui eu adiciono a nova carta a mão e removo ela da variavel em que estava guardada
                Descartar = input("Qual carta deseja descartar da sua mão? ")


                while not FuncoesJM.validar(Descartar,list(range(1,len(Mão)+1))) and Descartar != aceitar[10]:  #Aqui peguei o numero de cartas que tem na mão, transformei em uma lista para que possa funcionar na função que criei
                    print ('A carta "%s" não existe.'%Descartar)  #Mensagem informando que o usuario digitou uma carta que ele não possui na mão
                    Descartar = input("Qual carta deseja descartar da sua mão? ")  #Pergunto novamente qual carta ele deseja descartar


                if Descartar != aceitar[len(aceitar)-1]: # vejo se o usuario não desistiu de jogar enquanto descartava alguma carta


                    if int(Descartar) == len(Mão):  #Aqui vejo se o usuario quis descartar a carta nova que ele pegou
                        print("Descartou a nova carta") # Mensagem informando que ele descartou a nova carta


                    else:
                        print("Pegou a carta %s %s"%(Mão[len(Mão)-1][0],Mão[len(Mão)-1][1])) #Se ele não descartou a nova carta exibo a mensagem infromando a carta que ele oegiu
                    print("%s, você descartou a carta de nº%s : %s %s"%(JogadorVez, Descartar, Mão[int(Descartar)-1][0], Mão[int(Descartar)-1][1])) # Aqui mostro a carta que ele descartou
                    Descartadas.append(Mão.pop(int(Descartar)-1))  #Aqui adiciono a pilha de descartes a carta que o jogador da vez desscartou
                    Ganhou = FuncoesJM.vence(Mão) #uso minha função para ver se ele ganhou com a alteração que ele fez
                    time.sleep(4) #Tempo para o usuario ler as msg e passar o pc para o proximo jogador


            elif FuncoesJM.validar(str.lower(Jogada),aceitar[5:10]):  #vejo se o usuario nao quis a nova carta
                print("Você não quis a carta %s %s."%(NovaCarta[0][0],NovaCarta[0][1])) #Exibo a mensagem informando a carta que ele não quis 
                Descartadas.append(NovaCarta.pop()) # Aqui adiciono a carta que foi descartada para o baralho das "Descartadas" utilizando o metodo pop que exclui e salva o elemento
                time.sleep(2)


        if (len(BaralhoG)== 0): #Vejo se as cartas do jogo acabou e pergunto se o usuario deseja jogar retornando as cartas descartadas para o baralho novamente
            print ("As cartas acabaram, deseja traçar as cartas descartadas\ne fazer um novo deck ou empatar a partida?")
            print ("Desistir agora o Jogador(a) %s perde!"%JogadorVez)
            Decidir = input("Traçar ou Empatar?")


            while not FuncoesJM.validar(Decidir,["empatar", "traçar",aceitar[10]]): #Vejo se o usuario digitou algo legivel para aceitação
                print("Decisão invalida!") #Mensagem informando ao usuario
                Decidir = input("Traçar ou Empatar?")  #Peço para digitar novamente


            if str.lower(Decidir) == "empatar":
                empate = True


            elif str.lower(Decidir) == "traçar": # traço o baralho novamente juntado as cartas descartadas ao baralhoG vazio, aumentando seu indice
                BaralhoG += Descartadas      #Adiciono as descartadas ao baralho vazio
                random.shuffle(BaralhoG)                                                                                # Misturo os elementos/cartas chamando a função "shuffle"


        if Jogada == aceitar[10] or Descartar == aceitar[10] or Ganhou or Decidir == aceitar[10]: #Todas as decisões que param o Jogo estão aqui seguida da instrução que faz o codigo do jogo parar de repetir
            Parar = True     #Condição suprema de parada

        NumJogada+= 1  #Com essa variavel controlo o numero de jogadas


        

    if Jogada == aceitar[10] or Descartar == aceitar[10] or Decidir == aceitar[10]:  #Se o jogador desistir
        print ("O jogador(a) %s desistiu e %s é o(a) vencedor(a)."%(JogadorVez, OutroJogador)) #Aparecera uma mensagem nada animante, assim como a partida


    elif Ganhou:
        FuncoesJM.girarNomeGanhou(JogadorVez)
        FuncoesJM.fogos()  #A função tá soltando fogos pra sempre, alterar já que adcionou a possibilidade de jogar novamente após ter um ganhador


    else:
        if empate: #Caso deja empate na partida
            print("O jogo deu empate entre os jogadores %s e %s"%(Jogador1,Jogador2))

    if comando == '3':
        print("\n")
    else:
        JogarNovamente = input("Deseja iniciar um novo jogo? ")
        while not FuncoesJM.validar(JogarNovamente, aceitar[0:len(aceitar)-1]): #Controlo se o usuario digitou algo que esteja nos comandos
            if JogarNovamente == aceitar[10]: #Aqui explico caso o usuario digite o "/surrender"
                print ("O jogo acabou e não temos jogadores para você desistir.") #mensagem explicando
            print ('"%s" não está disponivel, tente novamente.'%JogarNovamente) #Mensagem avisano que não está disponivel
            JogarNovamente = input("Deseja iniciar um novo jogo? ") #Peço para me informar o novo dado
        if FuncoesJM.validar(JogarNovamente, aceitar[0:5]): #Aqui vejo se o usuario quis que o jogo começasse novamente 
            Novamente = True  #Variavel que faz com que o while se repita
            print("Um novo jogo vai começar!") #Mensagem informando
            time.sleep(3)
            print("\n"*42)
        else:
            Novamente = False
print ("Obrigado por jogar =)")
print ("Fechando o jogo...")
time.sleep(2)


