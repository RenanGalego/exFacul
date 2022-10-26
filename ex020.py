""" Interfáce Gráfica """

from msilib.schema import Icon
from tkinter import *

def clicarBotao():
    print("Deu certo Carai")

janelaPrincipal = Tk()
janelaPrincipal.geometry("500x300")
janelaPrincipal.title("Faculdade Estácio")

texto = Label(master=janelaPrincipal, text="Olá Mundo", font='Arial-Bold, 30')
texto.pack()

botao = Button(master=janelaPrincipal, text="Clique", command=clicarBotao)
botao.pack()

janelaPrincipal.mainloop()