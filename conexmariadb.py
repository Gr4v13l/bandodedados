import mysql.connector
# Definir as informações de conexão
config = {
  'user': 'usuarioremoto',
  'password': 'minhasenha',
  'host': '34.205.48.247',
  'database': 'animais_africanos'
}
# Estabelecer a conexão com o banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")
# Fechar a conexão
conn.close()
