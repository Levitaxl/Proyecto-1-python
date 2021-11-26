from models.UsersModel import UsersModel


class CountAllUsersService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        quantity = UsersModel.invoke()
        if(quantity==False):
            return quantity
        return len(quantity)