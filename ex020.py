""" Interfáce Gráfica """

from tkinter import *

janelaPrincipal = Tk()
janelaPrincipal.geometry("500x300")
janelaPrincipal.title("Faculdade Estácio")

texto = Label(master=janelaPrincipal, text="Olá Mundo", font='Arial-Bold, 30')
texto.place(x = 150, y = 100)

janelaPrincipal.mainloop()