from .connection import conectar

def criar_tabelas():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS pessoas (
            id SERIAL PRIMARY KEY,
            nome VARCHAR(100) NOT NULL
        );
    """)
    cur.execute("""
        CREATE TABLE IF NOT EXISTS telefones (
            id SERIAL PRIMARY KEY,
            id_pessoa INTEGER NOT NULL REFERENCES pessoas(id),
            telefone VARCHAR(20) NOT NULL
        );
    """)

    conn.commit()
    cur.close()
    conn.close()