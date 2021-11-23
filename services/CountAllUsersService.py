from models.CountAllUsersModel import CountAllUsersModel


class CountAllUsersService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        countAllUsersModel = CountAllUsersModel()
        quantity = countAllUsersModel.invoke()
        return (quantity)