from services.GetWinnerByAgeControllerAndGenderService import GetWinnerByAgeControllerAndGenderService

#Clase la que se encarga de gestionar de los servicios de obtener a los ganadores por grupo etario y genero.
class GetWinnerByAgeControllerAndGenderController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        winners = GetWinnerByAgeControllerAndGenderService.invoke()
        return winners