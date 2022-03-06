def encontrar_melhor_solucao(conjunto):
    soma_impares = sum(conjunto[::2])
    soma_pares = sum(conjunto[1::2])
    if soma_impares > soma_pares:
        return conjunto[::2]
    else:
        return conjunto[1::2]