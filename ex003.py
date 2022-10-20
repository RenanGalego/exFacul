valorUnidade = 10.00
unidade = int(input("Quantas unidades foram compradas? "))
valorCompra = 0
valorDesconto = 0

if unidade <= 10:
    valorCompra = valorUnidade*unidade
    print(f"Sem desconto, sua compra ficou em R${valorCompra :.2f}")
elif unidade <= 20:
    valorCompra = valorUnidade*unidade
    valorDesconto = valorCompra-(valorCompra*10/100)
    print(f"Valor com 10% de Desconto R${valorDesconto :.2f} / valor total R${valorCompra :.2f} ")
else:
    valorCompra = valorUnidade*unidade
    valorDesconto = valorCompra-(valorCompra*20/100)
    print(f"Valor com 20% de Desconto R${valorDesconto :.2f} / valor total R${valorCompra :.2f} ")