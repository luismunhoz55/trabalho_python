class Person:

    def __init__(self, nome, numero, cep):
     self.nome = nome
     self.numero = numero
     self.cep = cep

    def listarProps(self):
        print("Nome: "+self.nome)
        print("Número de telefone: "+self.numero)
        print("Cep: "+self.cep)
        
    def alterarNome(novoNome):
        self.nome = novoNome
        
    def alterarNumero(novoNumero):
        self.numero = novoNumero
        
    def alterarCep(novoCep):
        self.cep = novoCep
    