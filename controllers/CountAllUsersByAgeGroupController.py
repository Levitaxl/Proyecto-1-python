from services.CountAllUsersByAgeGroupService import CountAllUsersByAgeGroupService

#Clase la que se encarga de gestionar el servicio de contar todos los usuarios por grupo etario.
class CountAllUsersByAgeGroupController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        quantity = CountAllUsersByAgeGroupService.invoke()
        return quantity