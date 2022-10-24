""" Subprogramas """

n = int(input(f'Escolha a função 1 ou a função 2: '))

if n == 1:
    def func1(x):
        return x+1
    s = func1(10)
else:
    def func2(x):
        return x+2
    s=func2(20)

print(s)