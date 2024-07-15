# Cria um dicionário vazio para armazenar os pares usuário-senha
senhas = {}

def adicionar_senha():
    """Permite ao usuário adicionar um novo par usuário-senha."""
    usuario = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    senhas[usuario] = senha
    print("Senha adicionada com sucesso!")

def pesquisar_senha():
    """Permite ao usuário pesquisar uma senha pelo nome de usuário."""
    usuario = input("Digite o nome de usuário para pesquisar a senha: ")
    if usuario in senhas:
        print(f"A senha para '{usuario}' é: {senhas[usuario]}")
    else:
        print(f"Usuário '{usuario}' não encontrado.")

# Menu de opções
while True:
    print("\nOpções:")
    print("1. Adicionar senha")
    print("2. Pesquisar senha")
    print("3. Sair")
    escolha = input("Escolha uma opção (1/2/3): ")

    if escolha == '1':
        adicionar_senha()
    elif escolha == '2':
        pesquisar_senha()
    elif escolha == '3':
        print("Encerrando o programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")

# Lembre-se de salvar essas senhas de forma segura em um ambiente real!
