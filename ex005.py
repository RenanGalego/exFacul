""" Encontrar o menor valor de uma lista """

def valorMin(lista):
    minimo=lista[0]
    for elementos in lista:
        if elementos<minimo:
            minimo = elementos
    return minimo

listaTest = [0,-3,90,-4,-4.5, 102]
menor = valorMin(listaTest)
print(f'O menor valor encontrado foi {menor}')