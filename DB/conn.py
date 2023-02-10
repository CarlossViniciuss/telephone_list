import psycopg2

def conectar_banco():
    conn = psycopg2.connect(
        host="localhost",
        database="agenda",
        user="postgres",
        password="senha"
    )
    return conn