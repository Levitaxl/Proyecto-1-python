from services.GetAllUsersService import GetAllUsersService

class GetAllUsersController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        getAllUsersService = GetAllUsersService()
        users = getAllUsersService.invoke()
        return users