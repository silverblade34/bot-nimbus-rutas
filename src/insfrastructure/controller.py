from ..application.reponse import ResponseBot

class BotsRutasController():
    def __init__(self):
        
        self.responseData = ResponseBot()

    def controllerRutas(self, depot):
        list = self.responseData.parsedConsumirNimbus(depot)
        return list
