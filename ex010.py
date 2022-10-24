""" Parâmetros """

def taximetro(distancia, multiplicador=1):
    largada = 3
    km_rado = 2
    valor = (largada+distancia*km_rado)*multiplicador
    return valor

pagamento = taximetro(3.5)
print(f'Valor da corrida R$ {pagamento}')

