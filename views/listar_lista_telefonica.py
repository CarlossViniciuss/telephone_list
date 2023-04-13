from database.queries import criar_tabelas
from models.telephone_models import Telefones

# Função para listar todos os contatos da lista telefônica
def listar_lista_telefonica():
    criar_tabelas()
    Telefones.listar_lista_telefonica()
    