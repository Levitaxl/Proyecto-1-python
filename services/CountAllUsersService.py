from models.UsersModel import UsersModel

#Servicio con la logica de negocio, que se encarga de contar a los usuarios en el sistema.
class CountAllUsersService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        quantity = UsersModel.invoke()
        if(quantity==False):
            return quantity
        return len(quantity)