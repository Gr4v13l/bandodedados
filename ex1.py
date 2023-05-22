import mysql.connector

# Definir as informações de conexão
config = {
  'user': 'admin',
  'password': '12345678',
  'host': 'database-1.chfa7xigy3st.us-east-1.rds.amazonaws.com',
  'database': 'Brasil'
}

# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")

# Fechar a conexão
cursor = conn.cursor()