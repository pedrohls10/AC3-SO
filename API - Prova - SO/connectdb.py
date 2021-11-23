import mysql.connector 

def insert_db(nome,timeCoracao,jogadorPreferido):
    try:
        mydb = mysql.connector.connect(
            host= 'localhost',
            user= 'root',
            password= 'Pedro2212',
            database= 'dadosTorcida'
        )

        if mydb.is_connected():
            db_Info = mydb.get_server_info()
            print("Conectado ao MySQL Server versão ", db_Info)

            mycursor = mydb.cursor()
            query = "INSERT INTO tb_torcida(nome,timeCoracao,jogadorPreferido,data_hora) VALUES (%s, %s, %s,now())"

            valores = [nome, timeCoracao, jogadorPreferido]
            mycursor.execute(query, valores)
            mydb.commit()

            print(mycursor.rowcount, "registro inserido")
    except mysql.connector.Error as e:
        print("Erro ao conectar com o MySQL", e)
    finally:
        if(mydb.is_connected()):
            mycursor.close()
            mydb.close()
            print("Conexão com MySQL está fechada\n")
