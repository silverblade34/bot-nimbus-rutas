from ..application.reponse import ResponseBot

class BotsRutasController():
    def __init__(self):
        
        self.responseData = ResponseBot()

    # def controllerRutas(self, depot, token,ruc_empresa):
    #     list = self.responseData.parsedConsumirNimbus(depot, token,ruc_empresa)
    #     return list

    def controllerRutas(self, depot, token):
        list = self.responseData.parsedConsumirPuntos(depot, token)
        return list