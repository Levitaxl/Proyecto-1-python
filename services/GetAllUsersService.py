
from models.UsersModel import UsersModel


class GetAllUsersService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        users = UsersModel.invoke()
        return (users)