# Lista para guardar os alunos
alunos = []

# Função para cadastrar
def cadastrar():
    nome = input("Digite o nome do aluno: ")
    alunos.append(nome)
    print("Aluno cadastrado!\n")

# Função para alterar
def alterar():
    nome = input("Digite o nome do aluno que quer alterar: ")
    if nome in alunos:
        novo_nome = input("Digite o novo nome: ")
        indice = alunos.index(nome)  # pega a posição na lista
        alunos[indice] = novo_nome
        print("Aluno alterado!\n")
    else:
        print("Aluno não encontrado!\n")

# Função para excluir
def excluir():
    nome = input("Digite o nome do aluno que quer excluir: ")
    if nome in alunos:
        alunos.remove(nome)
        print("Aluno excluído!\n")
    else:
        print("Aluno não encontrado!\n")

# Função para listar
def listar():
    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.\n")
    else:
        print("Lista de alunos:")
        for i in range(len(alunos)):
            print(str(i+1) + " - " + alunos[i])
        print()  # linha em branco

# Loop principal do sistema
while True:
    opcao = input('Digite: 1 - Cadastrar, 2 - Alterar, 3 - Excluir, 4 - Listar, 5 - Sair do Sistema: ')

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        alterar()
    elif opcao == "3":
        excluir()
    elif opcao == "4":
        listar()
    elif opcao == "5":
        print('Sistema finalizado com sucesso!!!!')
        break
    else:
        print('Opção inválida!\n')
