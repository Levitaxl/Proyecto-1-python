from services.GetWinnerService import GetWinnerService

class GetWinnerController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        getAllUsersService = GetWinnerService()
        user = getAllUsersService.invoke()
        return user