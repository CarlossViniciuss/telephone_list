from database.connection import conectar
from database.queries import criar_tabelas

# Função para adicionar telefone a uma pessoa já cadastrada
def adicionar_telefone():
    criar_tabelas()
    nome = input("Digite o nome da pessoa que deseja adicionar um telefone: ")
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT id FROM pessoas WHERE nome = %s", (nome,))
    id_pessoa = cur.fetchone()
    if id_pessoa:
        telefone = input("Digite o telefone da pessoa: ")
        cur.execute("INSERT INTO telefones (id_pessoa, telefone) VALUES (%s, %s)", (id_pessoa[0], telefone))
        conn.commit()
        print(f"Telefone adicionado com sucesso para {nome}!")
    else:
        print("Pessoa não encontrada!")
    cur.close()
    conn.close()