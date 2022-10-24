""" Uma função que retorne a soma de todos os número pares de uma lista """

def numPar(n):
    par = (n%2==0)
    return par

def somarPar(lista):
    soma=0
    for elementos in lista:
        if numPar(elementos):
            soma+=elementos
        print(f'{elementos} + {soma}')
    return soma

listaTest = [2, 4,10]
soma = somarPar(listaTest)
print(f'As somas dos número páres da lista é: {soma}')