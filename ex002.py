""" Se a nota for maior ou igual a 7 - Estudante APROVADO
    Se a nota for menor que 7 e maior ou igual a 5 - Estudante em RECUPERAÇÃO
    Se a nota for menor que 5 - Estudante REPROVADO """

nota = float(input("Nota do aluno: "))

if nota < 5:
    print("Estudante REPROVADO!")
elif nota >= 5 and nota < 7:
    print("Estudante EM RECUPERAÇÃO")
else:
    print("Estudante APROVADO")