from database.connection import conectar
from database.queries import criar_tabelas

# Função para cadastrar uma pessoa
def cadastrar_pessoa():
    criar_tabelas()
    nome = input("Digite o nome da pessoa: ")
    telefone = input("Digite o telefone da pessoa: ")
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT id FROM pessoas WHERE nome = %s", (nome,))
    pessoa_existente = cur.fetchone()
    if pessoa_existente:
        print("Já existe uma pessoa cadastrada com esse nome!")
    else:
        cur.execute("INSERT INTO pessoas (nome) VALUES (%s) RETURNING id", (nome,))
        id_pessoa = cur.fetchone()[0]
        cur.execute("INSERT INTO telefones (id_pessoa, telefone) VALUES (%s, %s)", (id_pessoa, telefone))
        conn.commit()
        print("Pessoa cadastrada com sucesso!")
    cur.close()
    conn.close()