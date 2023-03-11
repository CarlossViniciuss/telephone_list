from database.connection import conectar
from database.queries import criar_tabelas

def listar_pessoas():
    criar_tabelas()
    conn = conectar()
    cur = conn.cursor()
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
    cur.close()
    conn.close()