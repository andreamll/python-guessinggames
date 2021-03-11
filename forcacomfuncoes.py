import random

def jogar():

    imprimir_mensagem_abertura()

    palavra_secreta = definir_palavra_secreta()

    #Inicia as variaveis de controle
    enforcou = False
    acertou = False

    #So pode errar ate 7x
    erros = 0
    max_erros = 7
    chutes_incorretos = []

    #Mostrar a palavra chutada para o usuarios com as letras corretas e os espacos para aquelas letras
    #que ainda nao adivinhou
    palavra_chutada = iniciar_palavra_chutada(palavra_secreta)

    #enquanto o jogador estiver no jogo
    while (not enforcou and not acertou):

        chute = pedir_chute_jogador()

        #varre a palavra e verifica se possui a letra informada pelo usuario
        achou_letra = conferir_chute_jogador(chute, palavra_secreta, palavra_chutada)

        #chutou uma letra que nao faz parte da palavra secreta
        if (not achou_letra):
            erros = contar_erros(chute, erros, max_erros, chutes_incorretos)
            enforcou = checar_se_enforcou(palavra_secreta, erros, max_erros)

        #chutou uma letra que faz parte da palavra secreta
        else:
            acertou = contar_acertos(palavra_secreta, palavra_chutada)
            mostrar_mensagem_final(acertou, palavra_chutada)

    #Finaliza o processamento
    print("Fim do Jogo")

##Funcoes Auxiliares##
def imprimir_mensagem_abertura():
    print("**************************")
    print("Bem vindo ao jogo de Forca")
    print("**************************")
    print()

def definir_palavra_secreta():
    # Relacao de palavras
    dicionario_palavras = (
        "Alice", "Amargo", "Amor", "Artista", "Astronauta", "Bailarina", "Banana", "Basquete", "Bebe", "Bilhete",
        "Cadeado",
        "Cadeira", "Calculadora", "Carteira", "Cego", "Comida", "Escola", "Escova", "Estatua", "Frio", "Futebol",
        "Internet", "Lapis", "Livro", "Lixo", "Maquina", "Massagem", "Médico", "Microbio", "Odio", "Pescador", "Pintor",
        "Policial", "Prancha", "Professor", "Romance", "Sacola", "Semente", "Sombra", "Vitoria", "Xadrez")

    # Define a palavra secreta
    index_random = random.randrange(0, len(dicionario_palavras))
    return dicionario_palavras[index_random]

def iniciar_palavra_chutada(palavra):
    return ["_" for letra in palavra]

def pedir_chute_jogador():
    chute = input("Informe uma letra: ")
    return chute.strip()
    print()

def mostrar_mensagem_final(acertou, palavra_chutada):
    if (acertou):
        print("Parabéns! Você adivinhou a palavra secreta!")
        mostrar_desenho_trofeu()
    else:
        letras_faltando = str(palavra_chutada.count('_'))
        print('Ainda faltam acertar {} letras'.format(letras_faltando))

def conferir_chute_jogador(chute, palavra_secreta, palavra_chutada):
    index = 0
    achou_letra = False

    for letra in palavra_secreta:

        # chutou uma letra que faz parte da palavra secreta
        if (chute.lower() == letra.lower()):
            palavra_chutada[index] = letra.lower()
            achou_letra = True

        index = index + 1

    return achou_letra

def contar_erros(chute, erros, max_erros, chutes_incorretos):
    erros = erros + 1
    print("Não há a letra {} na palavra secreta. Total de erros: {} de {} permitidos.".format(chute, erros, max_erros))
    print()

    chutes_incorretos.append(chute)
    print("Banco de letras já informadas: {}".format(chutes_incorretos))
    atualizar_enforcamento(erros)
    return erros

def checar_se_enforcou(palavra_secreta, erros, max_erros):
    # Atingiu o numero maximo de erros permitidos
    if (erros == max_erros):
        print("Oh-oh! Você foi enforcado! A palavra secreta era: {}".format(palavra_secreta))
        mostrar_desenho_caveira()
        enforcou = True
    else:
        enforcou = False

    return enforcou

def contar_acertos(palavra_secreta,palavra_chutada):
    index = 0
    acertou = True
    palavra_chutada_print = ""

    # verifica se ja acertou a palavra
    for letra in palavra_secreta:

        # varre a palavra chutada e confere com a palavra secreta
        if (palavra_chutada[index] != letra.lower()):
            acertou = False

        palavra_chutada_print = palavra_chutada_print + palavra_chutada[index]
        index = index + 1

    print(palavra_chutada_print)

    return acertou

def mostrar_desenho_caveira():
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

def mostrar_desenho_trofeu():
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def atualizar_enforcamento(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()
        print()

#se chamar diretamente este arquivo
if (__name__ == "__main__"):
    jogar()

