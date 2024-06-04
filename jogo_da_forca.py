import random

def escolher_palavra():
    palavras = ['python', 'programacao', 'desenvolvimento', 'computador', 'jogo']
    return random.choice(palavras)

def mostrar_forca(tentativas):
    estagios = [
        """
        -----
        |   |
            |
            |
            |
            |
        -----
        """,
        """
        -----
        |   |
        O   |
            |
            |
            |
        -----
        """,
        """
        -----
        |   |
        O   |
        |   |
            |
            |
        -----
        """,
        """
        -----
        |   |
        O   |
       /|   |
            |
            |
        -----
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
            |
            |
        -----
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
       /    |
            |
        -----
        """,
        """
        -----
        |   |
        O   |
       /|\\  |
       / \\  |
            |
        -----
        """
    ]
    return estagios[tentativas]

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = "_" * len(palavra)
    tentativas = 0
    max_tentativas = 6
    letras_adivinhadas = []

    print("Bem-vindo ao Jogo da Forca!")
    while tentativas < max_tentativas and "_" in palavra_oculta:
        print(mostrar_forca(tentativas))
        print("Palavra: ", " ".join(palavra_oculta))
        print("Letras adivinhadas: ", " ".join(letras_adivinhadas))
        letra = input("Adivinhe uma letra: ").lower()

        if letra in letras_adivinhadas:
            print("Você já adivinhou essa letra.")
        elif letra in palavra:
            letras_adivinhadas.append(letra)
            palavra_oculta = "".join([letra if letra == c else palavra_oculta[i] for i, c in enumerate(palavra)])
        else:
            letras_adivinhadas.append(letra)
            tentativas += 1
            print("Letra incorreta!")
    
    if "_" not in palavra_oculta:
        print("Parabéns! Você ganhou!")
    else:
        print(mostrar_forca(tentativas))
        print("Você perdeu! A palavra era: ", palavra)

if __name__ == "__main__":
    jogar()
