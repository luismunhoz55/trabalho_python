from Person import Person

lista = []

def adicionarPessoas():
    print("\nAdicionando pessoas")

    while(True):
        nome = input('Qual o nome da pessoa? (fim para terminar) ')
        if(nome == 'fim') :
            break
        numero = input('Qual o número de telefone da pessoa? ')
        cep = input("E qual o cep? ")
        pessoa = Person(nome, numero, cep)
        lista.append(pessoa)

    main()

def listarTodasAsPessoas():
    print("\nListando todas as pessoas:")

    for pessoa in lista:
        print('Nome: '+pessoa.nome)
        print('Número de telefone: ' +pessoa.numero)
        print("Cep: "+pessoa.cep)
        print()

    main()

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
            print("Foi encontrada " + str(len(pessoas)) + " pessoa: ")
        else:
            print("Foram encontradas "+str(len(pessoas))+" pessoas: ")

        for pessoa in pessoas:
            print('Nome: ' + pessoa.nome)
            print('Número de telefone: ' + pessoa.numero)
            print("Cep: " + pessoa.cep)
            print()

    main()
def main():
    print("\nBem vindo!")
    print('1 - Adicionar pessoas à lista')
    print('2 - Listas todas as pessoas')
    print('3 - Buscar uma pessoa pelo nome')
    print('Outro número - sair')

    num = int(input('Digite um número: '))

    if(num < 1 or num > 3):
        print("Finalizado")
        return

    if(num == 1):
        adicionarPessoas()

    if(num == 2):
        listarTodasAsPessoas()

    if(num == 3):
        buscarPessoa()

main()