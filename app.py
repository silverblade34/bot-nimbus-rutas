from src.insfrastructure.controller import BotsRutasController

# def main(depot, token,ruc_empresa):
#         try:
#                 _controller = BotsRutasController()
#                 #raw = _controller.controllerRutas(depot,token,ruc_empresa)
#                 raw = _controller.controllerRutas(depot,token,ruc_empresa)
#                 print(raw)
#         except Exception as err:
#                 print(err)

def main(depot, token):
        try:
                _controller = BotsRutasController()
                #raw = _controller.controllerRutas(depot,token,ruc_empresa)
                raw = _controller.controllerRutas(depot,token)
                print(raw)
        except Exception as err:
                print(err)    


# depot = input("DEPOT: ")
# token = input("TOKEN: ")
# ruc_empresa = input("RUC EMPRESA: ")
# main(depot,token,ruc_empresa)

depot = input("DEPOT: ")
token = input("TOKEN: ")
main(depot,token)


