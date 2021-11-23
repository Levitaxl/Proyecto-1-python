from services.CountAllUsersService import CountAllUsersService

class CountAllUsersController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        getAllUsersService = CountAllUsersService()
        quantity = getAllUsersService.invoke()
        return quantity