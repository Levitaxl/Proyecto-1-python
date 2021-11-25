from services.GetWinnerByAgeGroupService import GetWinnerByAgeGroupService

class GetWinnerByAgeController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        getAllUsersService = GetWinnerByAgeGroupService()
        users = getAllUsersService.invoke()
        return users