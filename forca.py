def exibir_forca(tentativas):
    estagios_forca = [
        """
           --------
           |      |
           |      
           |      
           |      
           |      
        --------- 
        """,
        """
           --------
           |      |
           |      O
           |      
           |      
           |      
        --------- 
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      
           |      
        --------- 
        """,
        """
           --------
           |      |
           |      O
           |     /|
           |      
           |      
        --------- 
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |      
           |      
        --------- 
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / 
           |      
        --------- 
        """,
        """
           --------
           |      |
           |      O
           |     /|\\
           |     / \\
           |      
        --------- 
        """
    ]
    print(estagios_forca[tentativas])

import random

def escolher_palavra():
    palavras = ["desenvolvimento", "tecnologia", "programacao", "python", ""]
    return random.choice(palavras)

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_'] * len(palavra)
    tentativas = 0
    letras_tentadas = []

    print("Bem-vindo ao Jogo da Forca!")
    print("Adivinhe a palavra:")
    print(' '.join(palavra_oculta))
    print()

    while tentativas < 6:
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_tentadas.append(letra)

        if letra in palavra:
            print("Letra correta!")
            for i in range(len(palavra)):
                if palavra[i] == letra:
                    palavra_oculta[i] = letra
        else:
            print("Letra errada!")
            tentativas += 1

        exibir_forca(tentativas)
        print(' '.join(palavra_oculta))
        print(f"Tentativas restantes: {6 - tentativas}")
        print()

        if '_' not in palavra_oculta:
            print("Parabéns! Você ganhou!")
            break

    if tentativas == 6:
        print("Você perdeu! A palavra correta era:", palavra)

    print("Obrigado por jogar!")

jogar()
