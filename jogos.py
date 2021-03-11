import forca
import adivinhacao

print("*************")
print("Menu de Jogos")
print("*************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Escolha um jogo: "))

if (jogo == 1):
    print("Iniciando o jogo da Forca....")
    forca.jogar()
else:
    print("Iniciando o jogo da Adivinhação ....")
    adivinhacao.jogar()
