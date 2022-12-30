from src.insfrastructure.controller import BotsRutasController

def main(depot):
        _controller = BotsRutasController()
        raw = _controller.controllerRutas(depot)
        print(raw)

main("8141")

