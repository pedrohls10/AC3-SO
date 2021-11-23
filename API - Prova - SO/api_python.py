from connectdb import *
import time
import sys
from datetime import datetime


obj = datetime.now()
data = obj.strftime("%d-%m-%y")


def pegarDados():

    while True:
        leitura1 = input("Deseja cadastrar um torcedor e seu time do coração ? \n 1.Sim \n 2.Não \n 3.Sair \n")

        if leitura1 == "1":
            nome = input("Nome do torcedor : ")
            timeCoracao = input("Time : ")
            jogadorPreferido = input("Jogador Preferido : ")
            insert_db(nome,timeCoracao,jogadorPreferido)
            pegarDados2()
        elif leitura1 == "2":
            print("Obrigado e volte mais tarde para cadastrar outros torcedores")
            break

        elif leitura1 == "3" :
            print("App encerrado!")
            sys.exit()
        else :
            print("Escolha invalida!")
            pegarDados()

def pegarDados2():
    leitura2 = input("Deseja cadastrar outro ? \n 1.Sim \n 2.Não \n 3.Sair \n")
    if leitura2 == "1":
        nome = input("Nome do torcedor : ")
        timeCoracao = input("Time : ")
        jogadorPreferido = input("Jogador Preferido : ")
        insert_db(nome,timeCoracao,jogadorPreferido)

    elif leitura2 == "2":
            print("Obrigado e volte mais tarde para cadastrar outros torcedores")
            pegarDados()

    elif leitura2 == "3":
        print("App encerrado!")
        sys.exit()

    else:
        print("Escolha invalida!")
        pegarDados()


pegarDados()



