def particao(A, esquerda, direita):
    pivo = A[esquerda]
    i = esquerda + 1
    j = direita

    while True:
        while i <= j and A[i] <= pivo:
            i += 1
        while A[j] >= pivo and j >= i:
            j -= 1

        if i >= j:
            break

        A[i], A[j] = A[j], A[i]

    A[esquerda], A[j] = A[j], A[esquerda]

    return j

def quicksort(A, esquerda, direita):
    if esquerda < direita:
        indice_pivo = particao(A, esquerda, direita)
        quicksort(A, esquerda, indice_pivo - 1)
        quicksort(A, indice_pivo + 1, direita)


lista = [3, 6, 8, 10, 1, 2, 5]
quicksort(lista, 0, len(lista) - 1)
print(lista)