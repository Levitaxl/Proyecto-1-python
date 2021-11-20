from services.AddANewRouteService import AddANewRouteService

class AddANewRouteController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        route= input("Ingrese la nueva ruta ")
        addANewRouteService = AddANewRouteService()
        response = addANewRouteService.invoke(route)
        return response