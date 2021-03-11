import random

def jogar():
    print("**************************")
    print("Bem vindo ao jogo de Forca")
    print("**************************")

    #Relacao de palavras
    dicionario_palavras = ("Amargo",	"Amor",	"Artista",	"Astronauta",	"Bailarina",	"Banana",	"Basquete",	"Bebe",	"Bilhete",	"Cadeado",	"Cadeira",	"Calculadora",	"Carteira",	"Cego",	"Comida",	"Escola",	"Escova",	"Estatua",	"Frio",	"Futebol",	"Internet",	"Lapis",	"Livro",	"Lixo",	"Maquina",	"Massagem",	"Médico",	"Microbio",	"Odio",	"Pescador",	"Pintor",	"Policial",	"Prancha",	"Professor",	"Romance",	"Sacola",	"Semente",	"Sombra",	"Vitoria",	"Xadrez")

    #Define a palavra secreta
    index_random = random.randrange(0,40)
    palavra_secreta = dicionario_palavras[index_random]
    ##print(palavra_secreta)

    #Inicia as variaveis de controle
    enforcou = False
    acertou = False

    #So pode errar ate 6x
    erros = 0
    max_erros = 6

    #Mostrar a palavra chutada para o usuarios com as letras corretas e os espacos para aquelas letras
    #que ainda nao adivinhou
    #palavra_chutada = []
    #for index in range(0,len(palavra_secreta)):
    #    palavra_chutada.append("_")
    palavra_chutada = ["_" for letra in palavra_secreta]

    while (not enforcou and not acertou):

        chute = input("Informe uma letra: ")
        chute = chute.strip()

        index = 0
        achou_letra = False

        #varre a palavra e verifica se possui a letra informada pelo usuario
        for letra in palavra_secreta:

            #chutou uma letra que faz parte da palavra secreta
            if (chute.lower() == letra.lower()):
                palavra_chutada[index] = letra.lower()
                achou_letra = True

            index = index + 1


        # chutou uma letra que nao faz parte da palavra secreta
        if (not achou_letra):
            erros = erros + 1
            print ("Não há a letra {} na palavra secreta. Total de erros: {} de {} permitidos.".format(chute,erros, max_erros))

            # Atingiu o numero maximo de erros permitidos
            if (erros == max_erros):
                print("Oh-oh! Você foi enforcado! A palavra secreta era: {}".format(palavra_secreta))
                enforcou = True


        # chutou uma letra que faz parte da palavra secreta
        else:

            index = 0
            acertou = True
            palavra_chutada_print = ""

            #verifica se ja acertou a palavra
            for letra in palavra_secreta:

                # varre a palavra chutada e confere com a palavra secreta
                if (palavra_chutada[index] != letra.lower()):
                    acertou = False

                palavra_chutada_print = palavra_chutada_print + palavra_chutada[index]
                index = index + 1

            print (palavra_chutada_print)

            if (acertou):
                 print("Parabéns! Você adivinhou a palavra secreta!")
            else:
                letras_faltando = str(palavra_chutada.count('_'))
                print('Ainda faltam acertar {} letras'.format(letras_faltando))

    #Finaliza o processamento
    print("Fim do Jogo")

if (__name__ == "__main__"):
    jogar()