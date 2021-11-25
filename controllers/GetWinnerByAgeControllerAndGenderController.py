from services.GetWinnerByAgeGroupService import GetWinnerByAgeGroupService
from services.GetWinnerByGenderService import GetWinnerByGenderService

class GetWinnerByAgeControllerAndGenderController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        getWinnerByAgeGroupService = GetWinnerByAgeGroupService()
        winnersByAgeGroup = getWinnerByAgeGroupService.invoke()


        getWinnerByGenderService = GetWinnerByGenderService()
        winnersByGender = getWinnerByGenderService.invoke()
        
        winners=dict()
        winners.update(winnersByAgeGroup)
        winners.update(winnersByGender)
        
        return winners