from services.GetWinnerByAgeGroupService import GetWinnerByAgeGroupService
from services.GetWinnerByGenderService import GetWinnerByGenderService

#Clase la que se encarga de gestionar de los servicios de obtener a los ganadores por grupo etario y genero.
class GetWinnerByAgeControllerAndGenderController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        winnersByAgeGroup = GetWinnerByAgeGroupService.invoke()
        winnersByGender = GetWinnerByGenderService.invoke()

        if(winnersByAgeGroup == False or winnersByGender==False):
            return False
        
        winners=dict()
        winners.update(winnersByAgeGroup)
        winners.update(winnersByGender)
        
        return winners