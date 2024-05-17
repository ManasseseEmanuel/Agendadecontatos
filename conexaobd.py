import mysql.connector

def create_database_if_not_exists():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password=""  # Insira a senha, se houver
        )
        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE IF NOT EXISTS contatos")

        print("Banco de dados 'contatos' verificado ou criado com sucesso!")

        mycursor.close()
        mydb.close()
    except mysql.connector.Error as err:
        print(f"Erro ao criar/verificar banco de dados 'contatos': {err}")

def connect():
    create_database_if_not_exists()

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Insira a senha, se houver
        database="contatos"
    )
    return mydb

