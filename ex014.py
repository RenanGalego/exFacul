""" Fatorial Recursiva """

""" def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fatorial(n-1) """

#-------------------------------------

""" Fatorial não Recursiva """

def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for i in range(2, n+1):
            fat = fat*i
        return fat

print(fatorial(10))