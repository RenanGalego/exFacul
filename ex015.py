""" Equação de 2º Grau """
import numpy as np

def entradaDados():
    coeficiente = quantidade = eval(input('Digite o valor do coeficiente: '))
    return coeficiente

def calcularDelta(a,b,c):
    delta = b*b-4*a*c
    return delta

def caulcularRaiz(a,b,c,delta):
    if delta < 0:
        resultado = 'A equação não possui raízes nos números reais.'
    elif delta==0:
        x = -b/(2*a)
        resultado = f'A equação possui apenas a raiz: {x}'
    else:
        x1 = (-b-np.sqrt(delta))/(2*a)
        x2 = (-b+np.sqrt(delta))/(2*a)
        resultado = f'A equação possui as raízes: {x1} e {x2}'
        return resultado

a=entradaDados()
b=entradaDados()
c=entradaDados()

delta=calcularDelta(a,b,c)

resultadoRaiz=caulcularRaiz(a,b,c,delta)
print(resultadoRaiz)