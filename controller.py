from view import View
from model import AcessToken, AcessDB, API
from datetime import datetime


class Controller:
    def __init__(self, Token, API):
        self.view = View()
        self.Token = Token
        self.API = API
    
    def inicio(self):
        opcao = self.view.inicio()

        while opcao != 7:
            if opcao == 1:
                self.view.imprimeStatusToken(self.Token.generateToken(), self.Token.getToken())
            
            if opcao == 2:
                result = self.API.getPlataforms()
                self.view.imprimeStatus(result)
            
            if opcao == 3:
                result = self.API.getPlataformVersion()
                self.view.imprimeStatus(result)
            opcao = self.view.menu()

if __name__ == "__main__":
    token = AcessToken()
    API = API(token)
    main = Controller(token, API)
    main.inicio()