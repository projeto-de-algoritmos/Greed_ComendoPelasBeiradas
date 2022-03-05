import random

conjunto = [8, 15, 3, 7, 2, 2, 15]
resposta_pessoa = []
resposta_computador = []

while conjunto:
    print(conjunto)
    resposta = int(input("Escolha um dos números das pontas: "))

    # Verificando se o input é mesmo um dos extremos
    while resposta != conjunto[0] and resposta != conjunto[len(conjunto)-1]:
        print("Resposta inválida!")
        resposta = int(input("Escolha um dos números das pontas: "))

    resposta_pessoa.append(resposta)

    # Implementando redução do conjunto após escolha do jogador
    conjunto.remove(resposta)

    resposta = random.choice([conjunto[0], conjunto[len(conjunto)-1]])
    print(conjunto)
    print("O computador escolheu: ", resposta)
    conjunto.remove(resposta)

    resposta_computador.append(resposta)

print("O resultado da pessoa foi:", sum (resposta_pessoa))
print('O resultado do computador foi:', sum(resposta_computador))

if sum(resposta_pessoa) < sum(resposta_computador):
    print ("As máquinas venceram!")
else:
    print ("Os humanos venceram !!1!")