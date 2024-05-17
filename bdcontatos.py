from conexaobd import connect

def insert(mydb, nome, numero='', email='', nascimento=''):
    try:
        mycursor = mydb.cursor()

        sql = "INSERT INTO contatos(nome, numero, email, nascimento) VALUES (%s, %s, %s, %s)"
        val = (nome, numero, email, nascimento)
        mycursor.execute(sql, val)

        mydb.commit()
        print(mycursor.rowcount, "Contato inserido com sucesso!")

        mycursor.close()
    except Exception as e:
        print(f"Erro ao inserir contato: {e}")

def listar_contatos(mydb):
    try:
        mycursor = mydb.cursor()

        mycursor.execute("SELECT nome FROM contatos")
        contatos = mycursor.fetchall()

        nomes = [contato[0] for contato in contatos]

        mycursor.close()
        return nomes
    except Exception as e:
        print(f"Erro ao listar contatos: {e}")
        return []
