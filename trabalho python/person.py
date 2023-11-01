class Person:
    def __init__(self, nome, numero, cep):
        self.nome = nome
        self.numero = numero
        self.cep = cep

    def showItems(self):
        print(self.nome)
        print(self.numero)
        print(self.cep)