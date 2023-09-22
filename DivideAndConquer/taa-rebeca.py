def mergeSort(A, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2
        mergeSort(A, inicio, meio)
        mergeSort(A, meio + 1, fim)
        merge(A, inicio, meio, fim)

def merge(A, inicio, meio, fim):
    tamEsq = meio - inicio + 1
    tamDir = fim - meio

    Esq = [0] * tamEsq
    Dir = [0] * tamDir

    for i in range(tamEsq):
        Esq[i] = A[inicio + i]

    for j in range(tamDir):
        Dir[j] = A[meio + 1 + j]

    idEsq = 0
    idDir = 0
    k = inicio

    while idEsq < tamEsq and idDir < tamDir:
        if Esq[idEsq] < Dir[idDir]:
            A[k] = Esq[idEsq]
            idEsq += 1
        else:
            A[k] = Dir[idDir]
            idDir += 1
        k += 1

    while idEsq < tamEsq:
        A[k] = Esq[idEsq]
        idEsq += 1
        k += 1

    while idDir < tamDir:
        A[k] = Dir[idDir]
        idDir += 1
        k += 1


A = [9, 11, 10, 5, 6, 7]
mergeSort(A, 0, len(A) - 1)
print("Array ordenado:", A)
