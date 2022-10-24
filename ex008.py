""" Função para ferivicar um Número Primo """
#n = n/1 or n/n
def n_primo(n):
    if (n<2):
        return False
    i = n//2
    while (i>1):
        if(n%i==0):
            return False
        i=i-1
        return True

def imprimir_resultado(numero, resultado):
    mensagem= f'O número {numero} NÃO É PRIMO.'
    if (resultado):
        mensagem=f'O número {numero} É PRIMO.'
    return mensagem

n = int(input(f'Verifique se o número é primo: '))
resultado = n_primo(n)
msg=imprimir_resultado(n, resultado)
print(msg)