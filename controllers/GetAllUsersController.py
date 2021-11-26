from services.GetAllUsersService import GetAllUsersService

#Clase la que se encarga de gestionar el servicio de obtener todos los usuarios en el sistema.
class GetAllUsersController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        users = GetAllUsersService.invoke()
        return users