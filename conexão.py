import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
    host = 'database-1.chfa7xigy3st.us-east-1.rds.amazonaws.com',
    user ='admin',
    password = '12345678',
    database = 'Brasil'
)

    return mydb