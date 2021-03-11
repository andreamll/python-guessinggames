import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de Adivinhação")
    print("********************************")

    #Define o numero secreto
    numero_secreto = random.randrange(1,101) #42


    #Usuario inicia com 1000 pontos. A cada erro, perde x pontos do total
    pontuacao = 1000

    #Define o nivel de dificuldade e, a partir dele, o numero de tentativas
    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))
    qtde_tentativas = 0

    if (nivel == 1):
        qtde_tentativas = 20
    elif (nivel == 2):
        qtde_tentativas = 10
    else:
        qtde_tentativas = 5


    #Rodadas e adivinhacao
    for rodada in range(1,qtde_tentativas+1):

        print("Tentativa {} de {}".format(rodada, qtde_tentativas))
        chute_str = input("Digite o seu número: ")
        chute = int(chute_str)

        if (chute < 1 or chute >100):
            print("Digite um número entre 1 e 100!")
            continue

        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        print("Você digitou ", chute_str)

        if (acertou):
            print("Você acertou. Sua pontuação atual é de {} pontos".format(pontuacao))
            break
        else:
            pontuacao = pontuacao - abs(numero_secreto - chute)
            print("Sua pontuação atual é de {} pontos".format(pontuacao))

            if (maior):
                print("Você errou. O seu chute foi maior do que o número secreto")
            elif (menor):
                print("Você errou. O seu chute foi menor do que o número secreto")


    #Se nao acertou, diz qual eh o numero secreto
    if (not acertou):
        print("O número secreto era: {}".format(numero_secreto))


    #Finaliza o processamento
    print("Fim do Jogo")

if (__name__ == "__main__"):
    jogar()