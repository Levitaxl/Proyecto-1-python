
from models.UsersModel import UsersModel
#Servicio con la logica de negocio, que se encarga de obtener a todos los usuarios en el sistema.

class GetAllUsersService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        users = UsersModel.invoke()
        return (users)