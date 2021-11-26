from services.GetWinnerByGenderService import GetWinnerByGenderService

#Clase la que se encarga de gestionar de los servicios de obtener a los ganadores por genero.
class GetWinnerByGenderController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        users = GetWinnerByGenderService.invoke()
        return users