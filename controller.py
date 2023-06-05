from view import View
from model import AcessToken, API

class Controller:
    def __init__(self, Token, API):
        self.view = View()
        self.Token = Token
        self.API = API
    
    def inicio(self):
        opcao = self.view.inicio()

        while opcao != 9:
            if opcao == 1:
                self.view.imprimeStatusToken(self.Token.generateToken(), self.Token.getToken())
            
            if opcao == 2:
                result = self.API.getPlataforms()
                self.view.imprimeStatus(result)

            if opcao == 3:
                result = self.API.getGenres()
                self.view.imprimeStatus(result)

            if opcao == 4:
                result = self.API.getGameModes()
                self.view.imprimeStatus(result)
            
            if opcao == 5:
                result = self.API.getCompanies()
                self.view.imprimeStatus(result)
            
            if opcao == 6:
                result = self.API.getGames()
                self.view.imprimeStatus(result)

            if opcao == 7:
                result = self.API.getCharacter()
                self.view.imprimeStatus(result)
            if opcao == 8:
                #Chama todos os métodos de popular as tabelas
                result = self.API.getPlataforms()
                self.view.imprimeStatus(result)
                result = self.API.getGenres()
                self.view.imprimeStatus(result)
                result = self.API.getGameModes()
                self.view.imprimeStatus(result)
                result = self.API.getCompanies()
                self.view.imprimeStatus(result)
                result = self.API.getGames()
                self.view.imprimeStatus(result)
                result = self.API.getCharacter()
                self.view.imprimeStatus(result)
            opcao = self.view.menu()

if __name__ == "__main__":
    token = AcessToken()
    API = API(token)
    main = Controller(token, API)
    main.inicio()