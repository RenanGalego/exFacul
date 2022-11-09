class Pessoa:
    #construtor
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)
#------------------------------------#
    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender
    
    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender

#Objeto Pessoa
pessoa1 = Pessoa("Renan","Rua Geuza da Costa")
pessoa2 = Pessoa("Karytta","Rua Costa e Silva")

#Imprimir os Objetos
print(f'Nome: {pessoa1.get_nome()}, Endereço: {pessoa1.get_ender()}')
print(f'Nome: {pessoa2.get_nome()}, Endereço: {pessoa2.get_ender()}')