from database.connection import conectar
from database.queries import criar_tabelas

# Função para listar todos os contatos da lista telefônica
def listar_lista_telefonica():
    criar_tabelas()
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT pessoas.nome, telefones.telefone FROM pessoas INNER JOIN telefones ON pessoas.id = telefones.id_pessoa")
    contatos = cur.fetchall()
    if contatos:
        print("=== Lista Telefônica ===")
        for contato in contatos:
            print(f"{contato[0]} - {contato[1]}")
    else:
        print("Não há contatos na lista telefônica!")
    cur.close()
    conn.close()