import random

### imprime mensagem de abertura do jogo
def jogar_forca():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    ###
    ### Carregar palavra secreta dp arquivo .txt
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()

    ###
    ### Adiciona o campo "_" para a palavra secreta
    letras_acertadas = ["_" for letra in palavra_secreta]

    ###
    ### Imprima a letra acertada
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    ###
    ### Caso erre a letra você tem 6 tentativas
    while (not acertou and not enforcou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        ### Marca a tentativa correta dentro da forca
        if (chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if (chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    print("Fim do jogo")
    
if(__name__=="__main__"):
    jogar_forca()