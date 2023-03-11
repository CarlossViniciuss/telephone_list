from database.connection import conectar
from database.queries import criar_tabelas

# Função para deletar uma pessoa e seus telefones
def deletar_pessoa():
    nome = input("Digite o nome da pessoa que deseja deletar: ")
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT id FROM pessoas WHERE nome LIKE %s", (f"%{nome}%",))
    id_pessoa = cur.fetchone()
    if id_pessoa:
        cur.execute("DELETE FROM telefones WHERE id_pessoa = %s", (id_pessoa[0],))
        cur.execute("DELETE FROM pessoas WHERE id = %s", (id_pessoa[0],))
        conn.commit()
        print(f"Pessoa {nome} e seus telefones foram deletados com sucesso!")
    else:
        print("Pessoa não encontrada!")
    cur.close()
    conn.close()