from services.AddANewRouteService import AddANewRouteService


#Clase la que se encarga de gestionar el servicio de agregar una nueva ruta y cargar archivos al sistema.

class AddANewRouteController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self,route):
        response = AddANewRouteService.invoke(route)
        return response