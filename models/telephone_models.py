from database.connection import conectar
conn = conectar()
cur = conn.cursor()

class Telefones:
    def listar_contatos(self, nome):
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

    def adicionar_telefone(self, nome):
        cur.execute("SELECT id FROM pessoas WHERE nome = %s", (nome,))
        id_pessoa = cur.fetchone()
        if id_pessoa:
            telefone = input("Digite o telefone da pessoa: ")
            cur.execute("INSERT INTO telefones (id_pessoa, telefone) VALUES (%s, %s)", (id_pessoa[0], telefone))
            conn.commit()
            print(f"Telefone adicionado com sucesso para {nome}!")
        else:
            print("Pessoa não encontrada!")

    def listar_lista_telefonica(self):
        cur.execute("SELECT pessoas.nome, telefones.telefone FROM pessoas INNER JOIN telefones ON pessoas.id = telefones.id_pessoa")
        contatos = cur.fetchall()
        if contatos:
            print("=== Lista Telefônica ===")
            for contato in contatos:
                print(f"{contato[0]} - {contato[1]}")
        else:
            print("Não há contatos na lista telefônica!")
