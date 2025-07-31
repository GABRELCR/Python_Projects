# A) Mensagem de boas-vindas com o nome
print("Olá, Usuário! Bem-vindo ao sistema de gerenciamento de livros de Gabriel Corrêa Rebustini!.")

# B) Inicialização da lista de livros e do ID global
lista_livro = []
id_global = 0

# C) Função para cadastrar um livro
def cadastrar_livro(id_livro):

    #Pergunta ao usuário nome, autor e editora do livro e armazena os dados em um dicionário que é adicionado à lista de livros.

    nome = input("Digite o nome do livro: ")
    autor = input("Digite o nome do autor: ")
    editora = input("Digite a editora do livro: ")
    livro = {'id': id_livro, 'nome': nome, 'autor': autor, 'editora': editora}
    lista_livro.append(livro.copy()) # Adiciona uma cópia para evitar alterações futuras

# D) Função para consultar livros
def consultar_livro():

    # Oferece opções de consulta de livros (todos, por ID, por autor) e exibe os resultados.
    # vi. Repete o menu de consulta até que o usuário escolha retornar ao menu principal.

    while True:
        # Menu para consulta dos livros
        print("\n--- Menu Consultar Livro ---")
        print("1. Consultar Todos")
        print("2. Consultar por Id")
        print("3. Consultar por Autor")
        print("4. Retornar ao menu principal")

        consulta = input("Digite a opção desejada: ")

        if consulta == '1':
            # i. Consultar Todos
            if not lista_livro:
                print("Nenhum livro cadastrado.")
            else:
                print("\n--- Todos os Livros ---")
                for livro in lista_livro:
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    print("-" * 20)

        elif consulta == '2':
            # ii. Consultar por Id
            try:
                id_busca = int(input("Digite o ID do livro que deseja consultar: "))
                encontrado = False
                for livro in lista_livro:
                    if livro['id'] == id_busca:
                        print("\n--- Livro Encontrado ---")
                        print(f"ID: {livro['id']}")
                        print(f"Nome: {livro['nome']}")
                        print(f"Autor: {livro['autor']}")
                        print(f"Editora: {livro['editora']}")
                        encontrado = True
                        break
                if not encontrado:
                    print("Livro com o ID informado não encontrado.")
            except ValueError:
                print("Por favor, digite um ID válido (número inteiro).")

        elif consulta == '3':
            # iii. Consultar por Autor
            autor_busca = input("Digite o nome do autor que deseja consultar: ")
            livros_encontrados = []
            for livro in lista_livro:
                if livro['autor'].lower() == autor_busca.lower():
                    livros_encontrados.append(livro)

            if livros_encontrados:
                print(f"\n--- Livros do Autor '{autor_busca}' ---")
                for livro in livros_encontrados:
                    print(f"ID: {livro['id']}")
                    print(f"Nome: {livro['nome']}")
                    print(f"Autor: {livro['autor']}")
                    print(f"Editora: {livro['editora']}")
                    print("-" * 20)
            else:
                print(f"Nenhum livro encontrado para o autor '{autor_busca}'.")

        elif consulta == '4':
            # iv. Retornar ao menu principal
            break
        else:
            # v. Opção inválida
            print("Opção inválida. Por favor, escolha uma das opções do menu.")

# E) Função para remover um livro
def remover_livro():

    # Pergunta ao usuário o ID do livro a ser removido e o remove da lista de livros.
    # Exibe uma mensagem se o ID for inválido.

    try:
        id_remover = int(input("Digite o ID do livro que deseja remover: "))
        removido = False

        for i, livro in enumerate(lista_livro):
            if livro['id'] == id_remover:
                del lista_livro[i]
                print(f"Livro com ID {id_remover} removido com sucesso.")
                removido = True
                break

        if not removido:
            print(f"Id inválido. Nenhum livro encontrado com o ID {id_remover}.")
    except ValueError:
        print("Por favor, digite um ID válido (número inteiro).")

# F) Menu principal (código principal - main)
if __name__ == "__main__":
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastrar Livro")
        print("2. Consultar Livro")
        print("3. Remover Livro")
        print("4. Encerrar Programa")

        opcao_principal = input("Digite a opção desejada: ")

        if opcao_principal == '1':
            # i. Cadastrar Livro
            id_global += 1
            cadastrar_livro(id_global)
        elif opcao_principal == '2':
            # ii. Consultar Livro
            consultar_livro()
        elif opcao_principal == '3':
            # iii. Remover Livro
            remover_livro()
        elif opcao_principal == '4':
            # iv. Encerrar Programa
            print("Encerrando o programa. Até logo!")
            break
        else:
            # v. Opção inválida
            print("Opção inválida. Por favor, escolha uma das opções do menu.")

# G) Implementação de lista de dicionários (já implementado em lista_livro)

# H) Inserção de comentários relevantes no código