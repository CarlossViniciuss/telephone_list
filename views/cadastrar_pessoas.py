from database.connection import conectar
from database.queries import criar_tabelas
from models.pessoas_models import Pessoas

# Função para cadastrar uma pessoa
def cadastrar_pessoa():
    criar_tabelas()
    nome = input("Digite o nome da pessoa: ")
    telefone = input("Digite o telefone da pessoa: ")

    pessoa_existente = Pessoas.consulta_pessoa_existente(nome)
    
    if pessoa_existente:
        print("Já existe uma pessoa cadastrada com esse nome!")
    else:
        pessoa_cadastrada = Pessoas.cadastro_pessoa(nome, telefone)
        print(f"Pessoa cadastrada com sucesso: {pessoa_cadastrada.id ,pessoa_cadastrada.nome, pessoa_cadastrada.telefone}")