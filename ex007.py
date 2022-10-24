""" Uma função que retorne o número fatorial """

#Estratégia 1(iterativa):
def func_iterativa(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

#Estratéga 2 (recursiva):
def fun_recursiva(n):
    if (n==0)or(n==1):
        return 1
    return n*fun_recursiva(n-1)

n=9
print(f'O fatoria de {n}! é : {func_iterativa(n)}!')
print(f'O fatoria de {n}! é : {fun_recursiva(n)}!')