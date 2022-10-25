""" Recursividade """

def contRegressiva(x):
    if x == -1:
        print('Acabou')
    else:
        print(x)
        contRegressiva(x-1)

contRegressiva(10)