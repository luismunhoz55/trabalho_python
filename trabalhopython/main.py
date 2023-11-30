from classes import Aluno, Professor, Nota
import os

alunos = []
professores = []

def adicionarAluno():
    os.system("cls")
    nome = input("Qual o nome do aluno? ")
    id = input("E qual sua id? ")

    for aluno in alunos:
        if(id == aluno.id):
            print("\nID já cadastrado!")
            return
    
    aluno = Aluno(nome, id)
    
    alunos.append(aluno)
    
    os.system("cls")

    print("Aluno criado!\n")
    aluno.exibirInformacoes()
    
    return

def adicionarProfessor():
    os.system("cls")
    nome = input("Qual o nome do professor? ")
    disciplina = input("Qual disciplina ele ensina? ")
    id = input("E qual sua id? ")

    for professor in professores:
        if(id == professor.id):
            print("\nID já cadastrado!")
            return
    
    professor = Professor(nome, disciplina, id)
    
    professores.append(professor)

    os.system("cls")    
    
    print("Professor criado!\n")
    professor.exibirInformacoes()
    
    return

def adicionarNotas():
    os.system("cls")
    id = input("Qual a id do professor? ")

    for professor in professores:
        
        if(professor.id == id):
            
            idAluno = input("Qual a id do aluno para adicionar as notas? ")

            for aluno in alunos:
                
                if(aluno.id == idAluno):
                    disciplina = professor.disciplina
                    notas = []

                    while True:
                        nota = int(input("Qual a nota a ser adicionada? (-1 para terminar): "))
                        
                        if(nota < 0 or nota > 10):
                            break
                        
                        notas.append(nota)

                    os.system("cls")
                    print()

                    professor.adicionarNotas(aluno, Nota(disciplina, notas))
                    return
                
            os.system("cls")    
            print("Aluno não encontrado")
            return
        
    os.system("cls")
    print("Professor não encontrado")
    return

def encontrarAluno():
    os.system("cls")
    print("Encontrar aluno")
    id = input("Qual o id do aluno? ")

    print("")

    for aluno in alunos:
        if(aluno.id == id):
            aluno.exibirInformacoes()
            return
    
    os.system("cls")
    print("Aluno não encontrado")
    return

def excluirAluno():
    os.system("cls")
    id = input("Qual a ID do aluno a ser excluído? ")
    indice = -1

    for i in range(len(alunos)):
        if(id == alunos[i].id):
            indice = i
            break

    if(indice != -1):
        print(f"Aluno excluido: {alunos[indice].nome}")
        alunos.pop(indice)
        return   

    print("Aluno não encontrado")
    return

def excluirProfessor():
    os.system("cls")
    id = input("Qual a ID do professor a ser excluído? ")
    indice = -1

    for i in range(len(professores)):
        if(id == professores[i].id):
            indice = i
            break

    if(indice != -1):
        print(f"Professor excluido: {professores[indice].nome}")
        professores.pop(indice)
        return   

    print("Professor não encontrado")
    return

while True:
    print("\nBem vindo!")
    print('1 - Adicionar aluno')
    print('2 - Adicionar professor')
    print('3 - Exibir todos os alunos')
    print('4 - Buscar um aluno e suas notas')
    print('5 - Exibir todos os professores')
    print('6 - Adicionar notas a um aluno')
    print('7 - Excluir um aluno')
    print('8 - Excluir um professor')
    print('Outro número - Sair')

    num = int(input('Digite um número: '))

    print()
    
    if(num < 1 or num > 8): 
        break
    
    elif(num == 1):
        adicionarAluno()
        
    elif(num == 2): 
        adicionarProfessor()   
        
    elif(num == 3):
        os.system("cls")

        if(len(alunos) > 0):
            print("Exibindo todos os alunos: \n")
            for aluno in alunos:
                aluno.exibirInformacoes()
                print()
        else:
            print("Nenhum aluno na lista")

    elif(num == 4):
        encontrarAluno()
    
    elif(num == 5):
        os.system("cls")

        if(len(professores) > 0):
            print("Exibindo todos os professores: \n")
            for professor in professores:
                professor.exibirInformacoes()
                print()
        else: 
            print("Nenhum professor na lista")
            
    elif(num == 6):
        adicionarNotas()

    elif(num == 7):
        excluirAluno()

    elif(num == 8):
        excluirProfessor()   
    
print("Programa finalizado")
