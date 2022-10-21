""" lista = [10,2,5,7,6,3]
soma=0
for i in range(len(lista)):
    if lista[i] %2 == 0:
        soma = soma+lista[i]
print(soma) """

lista = [10,2,5,7,6,3]
soma = 0

for i in lista:
    if i%2 == 0:
        soma += i
print(f'Soma dos elementos pares = {soma}')