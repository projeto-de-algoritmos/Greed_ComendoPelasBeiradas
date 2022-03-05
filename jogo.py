import random

conjunto = [8, 15, 3, 7]

while conjunto:
    print(conjunto)
    resposta = int(input("Escolha um dos números das pontas: "))

    # Verificando se o input é mesmo um dos extremos
    while resposta != conjunto[0] and resposta != conjunto[len(conjunto)-1]:
        print("Resposta inválida!")
        resposta = int(input("Escolha um dos números das pontas: "))

    # Implementando redução do conjunto após escolha do jogador
    conjunto.remove(resposta)

    resposta = random.choice([conjunto[0], conjunto[len(conjunto)-1]])
    print(conjunto)
    print("O computador escolheu: ", resposta)
    conjunto.remove(resposta)

