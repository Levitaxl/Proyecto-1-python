from services.AddANewRouteService import AddANewRouteService

class AddANewRouteController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self,route):
        response = AddANewRouteService.invoke(route)
        return response