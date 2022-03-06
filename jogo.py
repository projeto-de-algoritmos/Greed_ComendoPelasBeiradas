import random, guloso

resposta_pessoa = []
resposta_computador = []
conjunto = []


# Gerando um conjunto randômico inicial onde serão escolhidos 8 elementos de 0 até 99
for i in range(0,8,1):
    conjunto.append(random.randint(10,99))

# Iniciando e informando o andamento do jogo
while conjunto:
    # Turno do computador
    resposta = guloso.fazer_escolha(conjunto)
    print(conjunto)
    print("O computador escolheu: ", resposta)
    conjunto.remove(resposta)
    resposta_computador.append(resposta)

    # Turno do humano
    print(conjunto)
    resposta = int(input("Escolha um dos números das pontas: "))

    # Verificando se o input é mesmo um dos extremos
    while resposta != conjunto[0] and resposta != conjunto[len(conjunto)-1]:
        print("Resposta inválida!")
        resposta = int(input("Escolha um dos números das pontas: "))

    resposta_pessoa.append(resposta)
    conjunto.remove(resposta)

print ("\n\nFIM DE JOGO")
print("O resultado da pessoa foi:", sum (resposta_pessoa))
print("O resultado do computador foi:", sum(resposta_computador))

if sum(resposta_pessoa) < sum(resposta_computador):
    print ("As máquinas venceram!")
else:
    print ("Os humanos venceram !!1!")