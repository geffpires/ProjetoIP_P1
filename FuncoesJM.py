#Test Git
import time
def validar(variavel, aceitar):
    for x in aceitar:
        if str.lower(variavel) == str(x):
            return True
    else:
        return False


def vence(C, V=6):
    x = 0 #primeiro valor para indice
    Pares = [] #Crio uma lista para guardar os pares para que não interfira caso tenha uma outra carta repetida e e outra com apenas o sexo diferente
    while x < len(C): #Esse while tem uma função parecida com a de um for, para varer a lista, a diferença é que preciso do sempre alterar o valor do "x" quando um novo par é encontrado
        y = x + 1 #Porque com o indice de "x" irei pegar a carta a ser comparada com as do indice de "y" e não a motivos para comparar a carta com ela mesma :)
        par = False #Começo com esse valor boleano para indicar que ainda não achei nenhum par
        while y < len(C): # para varer a lista afim de achar o par da carta com indice "x"
            if C[x][0] == C[y][0] and C[x][1] != C[y][1]:  #Com essa condição vejo se as cartas do indice "x" e "y" formam um par
                #print("%s %s"%(C[x] , C[y]))
                carta = C[y] #Aqui guardo a carta do indice "y"
                Pares.append(C.pop(y))  # retiro primeiro a carta do indice "y" porque a carta do indice "y" vem depois da carta do indice "x", ou seja, se eu remover a do indice "x" irei alterar em que a carta do indice "y" estava
                Pares.append(C.pop(x))  #aqui ultilizo o indice que a carta foi encontrada para retirala e guardala nos pares
                par = True #Aqui altero o valor boleano se eu tiver encontrado o par da carta
                x = 0 #Indices, resete das cartas a serem comparadas já que os indices da lista das cartas da mão mudou
                y = x #Indices, reseto o tbm o indice das cartas para serem
            y += 1 #Indice, para percorer a lista afim de achar a carta encontrada
        if not par: #Esse valor boleano é para caso eu não tenha achado nenhum par com a carta de algum dos indices "x", caso eu tenha achado o valor logico dela sera alterado dentro do if
            x += 1 # A variavel que escolhe o indice da carta a ser comparada com as de mais
    C += Pares
    if (len(Pares)) == V:
        return True
    else:
        return False

def exibirCartas(c):
    for x in range(len(c)):
        if x % 2 == 0:
            a = x
        else:
            b = x
        if x == (len(c)-1) and x % 2 == 0:
            print("\n{0:^66}\n{1:^66}\n{2:^66}\n{1:^66}\n".format(("Carta de Nº%d: "%(x+1)),("#"*25),("#{0:^11}/{1:^11}#".format((c[x][0]),(c[x][1])))))   #Exibe a carta do topo da pilha de descartes

        elif x % 2 != 0:
            print("\n{0:^25}\t\t{1:^25}\n{2:^1}\t\t{2:^1}\n#{3:^11}/{4:^11}#\t\t#{5:^11}/{6:^11}#\n{2:^25}\t\t{2:^25}".format(("Carta de Nº%d"%(a+1)),("Carta de Nº%d"%(b+1)),("#"*25),(c[a][0]),(c[a][1]),(c[b][0]),(c[b][1])))


def girarNomeGanhou(Vencedor,Quant=6):
    if len(Vencedor) % 2 == 0:
        G = " Ganhou"
    else:
        G = " Ganhou!"
    for x in range(Quant):
        if x % 2 == 0:
            time.sleep(0.33)
            print("{0:^150}\n{1:^150}\n{2:^150}\n{1:^150}\n{0:^150}".format(("\n"*21),("*"*(len(Vencedor)+len(G))+"**"),("*%s%s*"%(Vencedor,G))))
            
        else:
            time.sleep(0.33)
            print("{0:^150}\n{1:^150}\n{2:^150}\n{1:^150}\n{0:^150}".format(("\n"*21),(" "),("%s%s"%(Vencedor,G))))


def fogos():         
    print("\n"*41)
    for x in range(3):
        print("\n\n\n\n      *\n                              *   *\n\n                            *       *\n\n                              *   *\n\n                                                                  *   *\n                                                                   * *\n                                                                * *   * *\n                                                                   * *\n            *   *                                                 *   *\n             * *\n          * * * * *\n             * *\n            *   *\n\n                                               * *\n                                              * * *\n                                               * *\n\n\n\n\n                      *   *\n                       * *\n                    * *   * *\n                       * *\n                      *   *\n\n\n                                                    *\n\n")
        time.sleep(0.25)
        print("\n"*41)
        print("\n\n\n     * *\n    * * *\n     * *\n\n\n\n\n\n                                                                  *   *\n\n                                                                *       *\n\n            *   *                                                 *   *\n             * *\n          * *   * *\n             * *\n            *   *\n                                              *   *\n                                               * *\n                                            * * * * *\n                                               * *\n                                              *   *\n\n\n                      *   *\n\n                    *       *\n\n                      *   *\n\n                                                   * *\n                                                  * * *\n                                                   * *\n")
        time.sleep(0.25)
        print("\n"*41)
        print("\n\n    *   *\n     * *\n  * * * * *\n     * *\n    *   *\n                                *\n\n\n\n\n\n\n\n            *   *\n\n          *       *\n\n            *   *\n                                              *   *\n                                               * *\n                                            * *   * *\n                                               * *\n                                              *   *\n\n\n\n\n\n\n\n                                                  *   *\n                                                   * *\n                                                * * * * *\n                                                   * *\n                                                  *   *")
        time.sleep(0.25)
        print("\n"*41)
        print("\n\n    *   *\n     * *\n  * *   * *\n     * *\n    *   *                      * *\n                              * * *\n                               * *\n\n\n\n\n                                                                    *\n\n\n\n\n\n\n                                              *   *\n\n                                            *       *\n\n                                              *   *\n\n\n\n\n                        *\n\n\n\n                                                  *   *\n                                                   * *\n                                                * *   * *\n                                                   * *\n                                                  *   *")
        time.sleep(0.25)
        print("\n"*41)
        print("\n\n    *   *\n\n  *       *\n                              *   *\n    *   *                      * *\n                            * * * * *\n                               * *\n                              *   *\n\n\n                                                                   * *\n                                                                  * * *\n                                                                   * *\n\n\n              *\n\n\n\n\n\n\n\n\n\n\n                     * *\n                    * * *\n                     * *\n\n                                                  *   *\n\n                                                *       *\n\n                                                  *   *")
        time.sleep(0.25)
        print("\n"*41)
        print("\n\n\n\n\n                              *   *\n                               * *\n                            * *   * *\n                               * *\n                              *   *\n\n                                                                  *   *\n                                                                   * *\n                                                                * * * * *\n                                                                   * *\n                                                                  *   *\n             * *\n            * * *\n             * *\n\n\n\n                                                *\n\n\n\n\n                    *   *\n                     * *\n                  * * * * *\n                     * *\n                    *   *\n\n\n\n")
        time.sleep(0.25)
        print("\n"*41)


def quantPar(C):
    aux = []
    aux.extend(C);
    x = 0 #primeiro valor para indice
    Pares = [] #Crio uma lista para guardar os pares para que não interfira caso tenha uma outra carta repetida e e outra com apenas o sexo diferente
    while x < len(aux): #Esse while tem uma função parecida com a de um for, para varer a lista, a diferença é que preciso do sempre alterar o valor do "x" quando um novo par é encontrado
        y = x + 1 #Porque com o indice de "x" irei pegar a carta a ser comparada com as do indice de "y" e não a motivos para comparar a carta com ela mesma :)
        par = False #Começo com esse valor boleano para indicar que ainda não achei nenhum par
        while y < len(aux): # para varer a lista afim de achar o par da carta com indice "x"
            if aux[x][0] == aux[y][0] and aux[x][1] != aux[y][1]:  #Com essa condição vejo se as cartas do indice "x" e "y" formam um par
                #print("%s %s"%(C[x] , C[y]))
                carta = aux[y] #Aqui guardo a carta do indice "y"
                Pares.append(aux.pop(y))  # retiro primeiro a carta do indice "y" porque a carta do indice "y" vem depois da carta do indice "x", ou seja, se eu remover a do indice "x" irei alterar em que a carta do indice "y" estava
                Pares.append(aux.pop(x))  #aqui ultilizo o indice que a carta foi encontrada para retirala e guardala nos pares
                par = True #Aqui altero o valor boleano se eu tiver encontrado o par da carta
                x = 0 #Indices, resete das cartas a serem comparadas já que os indices da lista das cartas da mão mudou
                y = x #Indices, reseto o tbm o indice das cartas para serem
            y += 1 #Indice, para percorer a lista afim de achar a carta encontrada
        if not par: #Esse valor boleano é para caso eu não tenha achado nenhum par com a carta de algum dos indices "x", caso eu tenha achado o valor logico dela sera alterado dentro do if
            x += 1 # A variavel que escolhe o indice da carta a ser comparada com as de mais
    print("\n{0:^66}".format(("Você tem %d par(es)"%(len(Pares)/2))))
    aux += Pares
