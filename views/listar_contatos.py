from database.queries import criar_tabelas
from models.telephone_models import Telefones

# Função para listar os contatos de uma pessoa
def listar_contatos():
    criar_tabelas()
    nome = input("Digite o nome da pessoa: ")
    
    Telefones.listar_contatos(nome)
