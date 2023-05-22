import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
    host = '34.205.48.247',
    user ='usuarioremoto',
    password = 'minhasenha',
    database = 'animais_africanos'
)

    return mydb