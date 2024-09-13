#teste

import random

def escolher_palavra():
    palavras = ['python', 'computacao', 'desenvolvimento', 'estudar', 'bootcamp', 'backend']
    return random.choice(palavras)

def exibir_palavra(palavra, letras_corretas):
    exibicao = ''
    for letra in palavra:
        if letra in letras_corretas:
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao

def jogar():
    palavra_secreta = escolher_palavra()
    letras_corretas = []
    tentativas = 6
    letras_erradas = []

    print('=-' * 20)
    print('        JOGO DA FORCA')
    print('=-' * 20)
    print(f"A palavra secreta tem {len(palavra_secreta)}, letras")
    print(exibir_palavra(palavra_secreta, letras_corretas))

    while tentativas > 0:
        tentativa = input("Digite uma letra: ").lower()

        if len(tentativa) != 1:
            print("Só pode digitar uma letra por vez.")
            continue

        if tentativa in letras_corretas or tentativa in letras_erradas:
            print("Essa letra já foi inserida. Tente outra.")
            continue

        if tentativa in palavra_secreta:
            letras_corretas.append(tentativa)
            print(f"A letra '{tentativa}' está na palavra secreta.")
        else:
            tentativas -= 1
            letras_erradas.append(tentativa)
            print(f"A letra '{tentativa}' não está na palavra secreta. Restam {tentativas} tentativas.")

        palavra_atualizada = exibir_palavra(palavra_secreta, letras_corretas)
        print(palavra_atualizada)

        if '_' not in palavra_atualizada:
            print(f"Parabéns! Você acertou a palavra: {palavra_secreta}.")
            break
    else:
        print(f"Poxa! Você perdeu. A palavra secreta era: {palavra_secreta}.")

jogar()