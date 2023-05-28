from decimal import *
from datetime import datetime

class View():
    def inicio(self):
        return self.menu()

    def menu(self):
        print("M E N U")
        print("1. Gerar token Twitch")
        print('2. Popular a tabela Plataformas')
        print('3. Popular a tabela Gêneros')
        print('4. Popular a tabela Companhias')
        print('5. Popular a tabela Jogos')
        print("7. Sair")
        opcao = int(input("Digite a opcao desejada : "))
        return opcao

    def imprimeStatusToken(self, status, token):
        if (status):
            print("Novo token: " + token)
        else:
            print(status)

    def imprimeStatus(self, status):
        if (status == 1):
            print("Carga realizada com sucesso!")
        else:
            print(status)

