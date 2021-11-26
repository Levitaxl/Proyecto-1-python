from services.CountAllUsersByGenderService import CountAllUsersByGenderService

#Clase la que se encarga de gestionar el servicio de contar todos los usuarios por genero.
class CountAllUsersByGenderController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        quantity = CountAllUsersByGenderService.invoke()
        return quantity