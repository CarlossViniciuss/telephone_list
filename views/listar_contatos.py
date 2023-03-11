from database.connection import conectar
from database.queries import criar_tabelas

# Função para listar os contatos de uma pessoa
def listar_contatos():
    criar_tabelas()
    nome = input("Digite o nome da pessoa: ")
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT id FROM pessoas WHERE nome LIKE %s", (f"%{nome}%",))
    id_pessoa = cur.fetchone()
    if id_pessoa:
        cur.execute("SELECT telefone FROM telefones WHERE id_pessoa = %s", (id_pessoa[0],))
        telefones = cur.fetchall()
        print(f"Telefones da pessoa {nome}:")
        for telefone in telefones:
            print(telefone[0])
    else:
        print("Pessoa não encontrada!")
    cur.close()
    conn.close()