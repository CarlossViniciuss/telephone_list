from models.telephone_models import Telefones

def buscar_por_nome():
    nome = input("Digite um nome para pesquisar: ")
    resultado = Telefones.buscar_por_nome(nome)
    if resultado:
        print(f"Nome enontrado: ID -> {resultado.id} / Nome -> {resultado.nome}")
    else:
        print("Nenhum resultado encontrado para o nome", nome)