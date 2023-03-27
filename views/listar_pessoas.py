from database.queries import criar_tabelas
from models.pessoas_models import Pessoas

def listar_pessoas():
    criar_tabelas()
    pessoas = Pessoas()
    pessoas.listar_pessoas()
    