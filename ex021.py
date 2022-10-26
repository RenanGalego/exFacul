""" Tratamento de Exceção """
op = 0
while op != 1:
    try:
        x = int(input("Digite um número inteiro: "))
        if x == 1:
            print("Fim do laço")
            break
        else:
            continue
    except ValueError:
        print("Eu disse número inteiro!")

