class Pessoa:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id

    def exibirInformacoes(self):
        print(f"Nome: {self.nome}")
        print(f"ID: {self.id}")


class Aluno(Pessoa):
    def __init__(self, nome, id):
        super().__init__(nome, id)
        self.notas = []

    def exibirInformacoes(self):
        super().exibirInformacoes()
        for nota in self.notas:
            print(f"Disciplina: {nota.disciplina}, notas: {nota.notas}")
            self.calcularMedia(nota.notas)
    
    def calcularMedia(self, notas):
        media = 0
        for nota in notas:
            media += nota
        
        media /= len(notas)
        print(f"Média: {media:.2f}")

class Professor(Pessoa):
    def __init__(self, nome, disciplina, id):
        super().__init__(nome, id)
        self.disciplina = disciplina

    def adicionarNotas(self, aluno, notas):
        aluno.notas.append(notas)
        print(f"Notas adicionadas para o aluno {aluno.nome} ({aluno.id}): Disciplina: {notas.disciplina}, {notas.notas}")

    def exibirInformacoes(self):
        super().exibirInformacoes()
        print(f"Disciplina: {self.disciplina}")

class Nota:
    def __init__(self, disciplina, notas):
        self.disciplina = disciplina
        self.notas = notas