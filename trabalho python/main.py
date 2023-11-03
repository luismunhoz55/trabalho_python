from pessoas import Person

import os

lista = []

def clear():
    os.system('cls')

def adicionarPessoas():
    print("\nAdicionando pessoas")

    while(True):
        nome = input('Qual o nome da pessoa? (fim para terminar) ')
        if(nome == 'fim'):
            clear()
            break
        numero = input('Qual o número de telefone da pessoa? ')
        cep = input("E qual o cep? ")
        pessoa = Person(nome, numero, cep)
        lista.append(pessoa)
        clear()

def listarTodasAsPessoas():
    print("\nListando todas as pessoas:")

    for pessoa in lista:
        pessoa.listarProps()
        print()

def buscarPessoa():
    nome = input("\nQual o nome da pessoa que você quer procurar? ").lower()

    pessoas = []

    for pessoa in lista:
        pessoaNome = pessoa.nome
        if(pessoaNome.lower() == nome):
            pessoas.append(pessoa)

    if(len(pessoas) == 0):
        print("Não foi encontrada nenhuma pessoa com esse nome")
    else:
        if(len(pessoas) == 1):
            print("\nFoi encontrada " + str(len(pessoas)) + " pessoa: ")
        else:
            print("\nForam encontradas "+str(len(pessoas))+" pessoas: ")

        for pessoa in pessoas:
            print('Nome: ' + pessoa.nome)
            print('Número de telefone: ' + pessoa.numero)
            print("Cep: " + pessoa.cep)
            print()

while True:
    print("\nBem vindo!")
    print('1 - Adicionar pessoas à lista')
    print('2 - Listas todas as pessoas')
    print('3 - Buscar uma pessoa pelo nome')
    print('Outro número - sair')

    num = int(input('Digite um número: '))

    if(num < 1 or num > 3):
        clear()
        print("Finalizado")
        break

    if(num == 1):
        clear()
        adicionarPessoas()

    if(num == 2):
        clear()
        listarTodasAsPessoas()

    if(num == 3):
        clear()
        buscarPessoa()
