from database.connection import conectar
from database.queries import criar_tabelas
from models.pessoas_models import Pessoas

# Função para deletar uma pessoa e seus telefones
def deletar_pessoa():
    criar_tabelas()
    nome = input("Digite o nome da pessoa que deseja deletar: ")

    Pessoas.deletar_pessoa(nome)