from services.GetWinnerByGenderService import GetWinnerByGenderService

class GetWinnerByGenderController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        users = GetWinnerByGenderService.invoke()
        return users