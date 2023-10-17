palavra_secreta = input("Digite uma palavra: ")

palavra_correta = ["_"] * len(palavra_secreta)

tentativas_maximas = 6

tentativas = 0

letras_usadas = []

while tentativas < tentativas_maximas:

    print("Palavra: " + " ".join(palavra_correta))

    letra = input("Digite uma letra: ").lower()

    if letra in letras_usadas:
        print("Você já usou essa letra. Tente outra.")
        continue

    letras_usadas.append(letra)

    if letra in palavra_secreta:
        print("Letra correta!")
        for i in range(len(palavra_secreta)):
            if palavra_secreta[i] == letra:
                palavra_correta[i] = letra
    else:
        print("Letra incorreta, tente novamente!")
        tentativas += 1
    if tentativas == 1:
        print(f"-------- \n"
              "|.     |  \n" 
              "|.     @  \n"
              "|.        \n"
              "|.        \n"
              "|.        \n"
              "Restam 5 tentativas! ")
    elif tentativas == 2:
        print("--------   \n"
              "|.     |   \n"
              "|.     @   \n"
              "|.    /    \n"
              "|.         \n"
              "|.         \n"
              "Restam 4 tentativas! ")
    elif tentativas == 3:
        print("--------  \n"
              "|.     |  \n"
              "|.     @  \n"
              "|.    /|  \n"
              "|.        \n"
              "|.        \n"
              "Restam 3 tentativas! ")
    elif tentativas == 4:
        print("--------  \n"
              "|.     |  \n"
              "|.     @  \n"
              "|.    /|\ \n"
              "|.        \n"
              "|.        \n"
              "Restam 2 tentativas! ")
    elif tentativas == 5:
        print("--------   \n"
              "|.     |   \n"
              "|.     @   \n"
              "|.    /|\  \n"
              "|.    /    \n"
              "|.         \n"
              "Restam apenas 1 tentativa!")
    elif tentativas == 6:
        print("--------   \n"
              "|.     |   \n"
              "|.     @   \n"
              "|.    /|\  \n"
              "|.    / \  \n"
              "|.         \n"
              "Você Perdeu!")

    if "".join(palavra_correta) == palavra_secreta:
        print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
        break

if tentativas == tentativas_maximas:
    print("A palavra correta era: ", palavra_secreta)