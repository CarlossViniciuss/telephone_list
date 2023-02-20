# -*- coding: utf-8 -*-
from DB.repository.repository import *

def menu():
    print("""
        Agenda Telefônica
        1 - Cadastrar Pessoa
        2 - Listar Pessoas
        3 - Adicionar Contato
        4 - Sair
    """)
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        criar_tabela()
        cadastrar_pessoa(nome, telefone)
    elif opcao == 2:
        criar_tabela()
        pessoas = listar_pessoas()
        for i, pessoa in enumerate(pessoas):
            print(f"{i + 1} - {pessoa[1]} - {pessoa[2]}")
    elif opcao == 3:
        criar_tabela()
        pessoas = listar_pessoas()
        for i, pessoa in enumerate(pessoas):
            print(f"{i + 1} - {pessoa[1]}")
        pessoa_id = int(input("Selecione a pessoa que deseja adicionar um contato: "))
        contato_id = int(input("Selecione a pessoa que deseja adicionar como contato: "))
        adicionar_contato(pessoas[pessoa_id - 1][0], pessoas[contato_id - 1][0])
    elif opcao == 4:
        print("Saindo...")
        exit()
    else:
        print("Opção inválida.")
menu()