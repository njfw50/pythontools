import sqlite3

db_file = 'liberty.db' # O nome do seu arquivo de banco de dados

try:
    # Conecta ao banco de dados SQLite
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    print("--- Tabelas no banco de dados ---")
    # Consulta para listar todas as tabelas no banco de dados
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if not tables:
        print("Nenhuma tabela encontrada neste banco de dados.")
    else:
        for table in tables:
            table_name = table[0]
            print(f"\n### Schema da tabela: '{table_name}' ###")
            # Consulta para obter informações de cada coluna da tabela
            cursor.execute(f"PRAGMA table_info({table_name});")
            columns = cursor.fetchall()
            if not columns:
                print(f"  Nenhuma coluna encontrada para a tabela '{table_name}'.")
            else:
                print("  Nome da Coluna | Tipo | Pode ser Nulo | Chave Primária")
                print("  ----------------------------------------------------")
                for col in columns:
                    col_name = col[1]
                    col_type = col[2]
                    not_null = "Não" if col[3] else "Sim"
                    is_pk = "Sim" if col[5] else "Não"
                    print(f"  {col_name:<14} | {col_type:<4} | {not_null:<13} | {is_pk:<14}")

except sqlite3.Error as e:
    print(f"Ocorreu um erro ao conectar ou consultar o banco de dados: {e}")
finally:
    # Garante que a conexão com o banco de dados seja fechada
    if conn:
        conn.close()
        print("\nConexão com o banco de dados fechada.")
