import psycopg2

# Função para conectar ao banco de dados
def conectar():
    conn = psycopg2.connect(
        host="localhost",
        database="minha_agenda",
        user="meu_usuario",
        password="minha_senha"
    )
    return conn

