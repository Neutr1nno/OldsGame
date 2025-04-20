sairJogo = 0

def criarMatriz():
     return [[0,0,0],
            [0,0,0],
            [0,0,0]]

def oldsGame(matrizLocal):
    for i in range(len(matrizLocal)):
        for j in range(len(matrizLocal[i])):
            print("X" if matrizLocal[i][j] == 1 else "O" if matrizLocal[i][j] == 2 else " ", end=" | "if j !=2 else "")
        print()
        print("-"*9) if i != 2 else print()


def verificarVitoria (matrizLocal, jogadorAtual):
     venceuDiagonalPrincipal = True
     venceuDiagonalInvertida = True
     for linha in matrizLocal:
          venceuLinha = True
          for coluna in linha:
               if coluna != jogadorAtual:
                    venceuLinha = False
          if venceuLinha:
               break
     for coluna in range(3):
          venceuColuna = True
          for linha in range(3):
               if matrizLocal[linha][coluna] != jogadorAtual:
                    venceuColuna = False
          if venceuColuna:
               break
     for i in range(3):
          if matrizLocal[i][i] != jogadorAtual:
               venceuDiagonalPrincipal = False
     for i in range(3):
          if matrizLocal[i][2-i] != jogadorAtual:
               venceuDiagonalInvertida = False
     return venceuLinha or venceuColuna or venceuDiagonalPrincipal or venceuDiagonalInvertida

def pegarCoordenadas(matrizLocal, jogadorAtual):
        print("Vez do jogador ","X" if jogadorAtual == 1 else "O")
        linha = int(input("Escolha a linha [0, 1, 2]: "))
        coluna = int(input("Escolha a coluna [0, 1, 2]: "))
        print()
        if linha not in [0, 1, 2]:
            print("O valor precisa ser 1, 2 ou 3.")
            pegarCoordenadas(matrizLocal, jogadorAtual)
        elif coluna not in [0, 1, 2]:
            print("O valor precisa ser 1, 2 ou 3.")
            pegarCoordenadas(matrizLocal, jogadorAtual)
        elif matrizLocal[linha][coluna] != 0:
            print("Esse espaço já está marcado")
            pegarCoordenadas(matrizLocal, jogadorAtual)
        else:
             matrizLocal[linha][coluna] = jogadorAtual   
             oldsGame(matrizLocal)

while sairJogo == 0:
    matriz = criarMatriz()
    oldsGame(matriz)

    for i in range(9):
        pegarCoordenadas(matriz, (i%2)+1)
        if verificarVitoria(matriz, (i%2)+1):
           print("Jogador ","X" if (i%2)+1==1 else "O"," ganhou a partida!!")
           break
        elif i == 8:
             print("Jogadores empataram!!")

    sairJogo = int(input("Você quer sair do jogo?\n\n[0] = Não \n[1] = Sim\n\n: "))
    