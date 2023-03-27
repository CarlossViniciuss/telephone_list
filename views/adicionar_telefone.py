from database.queries import criar_tabelas
from models.telephone_models import Telefones

# Função para adicionar telefone a uma pessoa já cadastrada
def adicionar_telefone():
    criar_tabelas()
    nome = input("Digite o nome da pessoa que deseja adicionar um telefone: ")
    telefones = Telefones()
    telefones.adicionar_telefone(nome)
