from views.adicionar_telefone import adicionar_telefone
from views.cadastrar_pessoas import cadastrar_pessoa
from views.deletar_pessoas import deletar_pessoa
from views.listar_contatos import listar_contatos
from views.listar_lista_telefonica import listar_lista_telefonica
from views.listar_pessoas import listar_pessoas

# Função para exibir o menu da aplicação
def menu():
    print("==== Lista Telefônica ====")
    print("1 - Cadastrar pessoa")
    print("2 - Listar contatos")
    print("3 - Deletar pessoa")
    print("4 - Listar todas as pessoas")
    print("5 - Adicionar telefone")
    print("6 - Listar lista telefônica")
    print("7 - Sair")

# Loop principal da aplicação
while True:
    menu()
    opcao = input("Digite uma opção: ")
    if opcao == "1":
        cadastrar_pessoa()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        deletar_pessoa()
    elif opcao == "4":
        listar_pessoas()
    elif opcao == "5":
        adicionar_telefone()
    elif opcao == "6":
        listar_lista_telefonica()
    elif opcao == "7":
        break
    else:
        print("Opção inválida!")
