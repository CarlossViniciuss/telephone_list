from database.connection import conectar
conn = conectar()
cur = conn.cursor()

class Pessoas:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    @staticmethod
    def consulta_pessoa_existente(nome):
        cur.execute("SELECT id FROM pessoas WHERE nome = %s", (nome,))
        return cur.fetchone()

    @staticmethod
    def cadastro_pessoa(nome, telefone):
        cur.execute("INSERT INTO pessoas (nome) VALUES (%s) RETURNING id", (nome,))
        id_pessoa = cur.fetchone()[0]
        cur.execute("INSERT INTO telefones (id_pessoa, telefone) VALUES (%s, %s)", (id_pessoa, telefone))
        conn.commit()

    @staticmethod
    def deletar_pessoa(self, nome):
        cur.execute("SELECT id FROM pessoas WHERE nome LIKE %s", (f"%{nome}%",))
        id_pessoa = cur.fetchone()
        if id_pessoa:
            cur.execute("DELETE FROM telefones WHERE id_pessoa = %s", (id_pessoa[0],))
            cur.execute("DELETE FROM pessoas WHERE id = %s", (id_pessoa[0],))
            conn.commit()
            print(f"Pessoa {nome} e seus telefones foram deletados com sucesso!")
        else:
            print("Pessoa não encontrada!")

    @staticmethod
    def listar_pessoas():
        cur.execute("SELECT COUNT(*) FROM pessoas")
        total_pessoas = cur.fetchone()[0]
        num_paginas = (total_pessoas // 10) + 1
        for pagina in range(num_paginas):
            cur.execute("SELECT id, nome FROM pessoas ORDER BY nome LIMIT 10 OFFSET %s", (pagina * 10,))
            pessoas = cur.fetchall()
            print(f"=== Página {pagina+1} de {num_paginas} ===")
        for pessoa in pessoas:
            print(f"{pessoa[0]} - {pessoa[1]}")
            print("\n")

