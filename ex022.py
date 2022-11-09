""" Tratamento de erro divisão por 0 """

def divisor(x,y):
    try:
        resultado = x/y
        print(f'Resultado de {x}/{y} é {resultado}')
    except ZeroDivisionError:
        print("Não se faz divisão por zero!")

divisor(3,9)