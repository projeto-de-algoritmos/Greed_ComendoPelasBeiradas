import random, guloso

resposta_pessoa = []
resposta_computador = []

conjunto = []
for i in range(0,8,1):
    conjunto.append(random.randint(10,99))

while conjunto:

    #resposta = random.choice([conjunto[0], conjunto[len(conjunto)-1]])
    resposta = guloso.fazer_escolha(conjunto)

    print(conjunto)
    print("O computador escolheu: ", resposta)
    conjunto.remove(resposta)
    resposta_computador.append(resposta)

    print(conjunto)
    resposta = int(input("Escolha um dos números das pontas: "))

    # Verificando se o input é mesmo um dos extremos
    while resposta != conjunto[0] and resposta != conjunto[len(conjunto)-1]:
        print("Resposta inválida!")
        resposta = int(input("Escolha um dos números das pontas: "))

    resposta_pessoa.append(resposta)

    # Implementando redução do conjunto após escolha do jogador
    conjunto.remove(resposta)

print("O resultado da pessoa foi:", sum (resposta_pessoa))
print('O resultado do computador foi:', sum(resposta_computador))

if sum(resposta_pessoa) < sum(resposta_computador):
    print ("As máquinas venceram!")
else:
    print ("Os humanos venceram !!1!")