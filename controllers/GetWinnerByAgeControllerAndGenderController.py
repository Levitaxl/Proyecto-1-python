from services.GetWinnerByAgeGroupService import GetWinnerByAgeGroupService
from services.GetWinnerByGenderService import GetWinnerByGenderService

class GetWinnerByAgeControllerAndGenderController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        winnersByAgeGroup = GetWinnerByAgeGroupService.invoke()
        if(winnersByAgeGroup == False):
            return False
        winnersByGender = GetWinnerByGenderService.invoke()
        if(winnersByGender == False):
            return False
        
        winners=dict()
        winners.update(winnersByAgeGroup)
        winners.update(winnersByGender)
        
        return winners