from services.GetWinnerService import GetWinnerService


#Clase la que se encarga de gestionar de los servicios de obtener al ganador.
class GetWinnerController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        user = GetWinnerService.invoke()
        return user