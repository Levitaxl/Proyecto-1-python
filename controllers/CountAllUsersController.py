from services.CountAllUsersService import CountAllUsersService

class CountAllUsersController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        quantity = CountAllUsersService.invoke()
        return quantity