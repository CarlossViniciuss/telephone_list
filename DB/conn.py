import psycopg2

def conectar_banco():
    conn = psycopg2.connect(
        host="localhost",
        database="minha_agenda",
        user="meu_usuario",
        password="minha_senha"
    )
    return conn