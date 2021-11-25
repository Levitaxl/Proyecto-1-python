from services.GetWinnerByGenderService import GetWinnerByGenderService

class GetWinnerByGenderController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        getAllUsersService = GetWinnerByGenderService()
        users = getAllUsersService.invoke()
        return users