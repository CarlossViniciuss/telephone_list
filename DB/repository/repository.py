#########################
# REPOSITORIO DE QUERYS #
#########################

from DB.conn import conectar_banco

####################################################################

def criar_tabela():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS pessoas (
            id serial PRIMARY KEY,
            nome varchar(255) NOT NULL,
            telefone varchar(255) NOT NULL
        );
    """
    )
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contatos (
            id serial PRIMARY KEY,
            pessoa_id integer REFERENCES pessoas(id),
            contato_id integer REFERENCES pessoas(id)
        );
    """)
    conn.commit()
    cursor.close()
    conn.close()

####################################################################

def cadastrar_pessoa(nome, telefone):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO pessoas (nome, telefone)
        VALUES (%s, %s);
    """, (nome, telefone))
    conn.commit()
    cursor.close()
    conn.close()

####################################################################

def listar_pessoas():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM pessoas;
    """)
    pessoas = cursor.fetchall()
    cursor.close()
    conn.close()
    return pessoas

####################################################################

def adicionar_contato(pessoa_id, contato_id):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contatos (pessoa_id, contato_id)
        VALUES (%s, %s);
    """, (pessoa_id, contato_id))
    conn.commit()
    cursor.close()
    conn.close()

####################################################################


