class Pessoa:
    #construtor
    def __init__(self, nome, ender, idade, cpf):
        self.set_nome(nome)
        self.set_ender(ender)
        self.set_idade(idade)
        self.set_cpf(cpf)
#------------------------------------#
    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender

    def set_idade(self, idade):
        self.idade = idade

    def set_cpf(self, cpf):
        self.cpf = cpf
    
    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender

    def get_idade(self):
        return self.idade

    def get_cpf(self):
        return self.cpf

