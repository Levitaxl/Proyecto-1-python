
import globales
from models.GetAllUsersModel import GetAllUsersModel


class GetAllUsersService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        getAllUsersModel = GetAllUsersModel()
        users = getAllUsersModel.invoke()
        return (users)