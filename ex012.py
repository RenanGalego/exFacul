""" Subprogramas Aninhados """

def taximetro(distancia):
    def culculaMult():
        if distancia < 5:
            return 1.5
        else:
            return 1
    multiplicador = culculaMult()
    largada = 3
    kmRodado = 2
    valor = (largada+distancia*kmRodado)*multiplicador
    return valor

distancia = float(input(f"Entre com a distância a ser percorrida em km: "))
pagamento = taximetro(distancia)
print(f'O valor total da corrida será de R$ {pagamento :.2f}')