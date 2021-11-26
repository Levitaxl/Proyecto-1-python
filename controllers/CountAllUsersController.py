from services.CountAllUsersService import CountAllUsersService

#Clase la que se encarga de gestionar el servicio de contar todos los usuarios en el sistema.
class CountAllUsersController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        quantity = CountAllUsersService.invoke()
        return quantity