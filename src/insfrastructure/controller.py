from ..application.reponse import ResponseBot

class BotsRutasController():
    def __init__(self):
        
        self.responseData = ResponseBot()

    def controllerRutas(self, depot, token,ruc_empresa):
        list = self.responseData.parsedEstructuraRutas(depot, token,ruc_empresa)
        return list

    def controllerPuntos(self, depot, token):
        list = self.responseData.parsedMostrarRutasPuntos(depot, token)
        return list
