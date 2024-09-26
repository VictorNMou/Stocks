import psycopg2

# Conexão com o banco de dados PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="database",
    user="admin",
    password="Venezia18"
)

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()
cursor.execute("SELECT version();")

# Buscar o resultado e imprimir
record = cursor.fetchone()
print(f"Conectado ao PostgreSQL - Versão: {record}")

# Fechar a conexão
cursor.close()
conn.close()