from src.insfrastructure.controller import BotsRutasController

def main(depot, token,ruc_empresa, funcion):
        try:
                if(1==int(funcion)):
                        _controller = BotsRutasController()
                        raw = _controller.controllerRutas(depot,token,ruc_empresa)
                        print(raw)
                else:
                     _controller = BotsRutasController()
                     raw = _controller.controllerPuntos(depot,token)
                     print(raw)  
        except Exception as err:
                print(err)
     



depot = input("DEPOT: ")
token = input("TOKEN: ")
ruc_empresa = input("RUC EMPRESA: ")
funcion = input("(Estructura rutas SMQ=1 , Puntos=2) : ")
main(depot,token,ruc_empresa, funcion)

