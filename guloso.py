def melhor_solucao(conjunto):
    soma_impares = sum(conjunto[::2])
    soma_pares = sum(conjunto[1::2])
    if soma_impares > soma_pares:
        return conjunto[::2]
    else:
        return conjunto[1::2]

def fazer_escolha(conjunto):
    extrema_esquerda = conjunto[0]
    extrema_direita = conjunto[len(conjunto) - 1]
    if extrema_esquerda in melhor_solucao(conjunto):
        return extrema_esquerda
    else:
        return extrema_direita
