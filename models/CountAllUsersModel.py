import globales
from models.LoadFileModel import LoadFileModel


class CountAllUsersModel:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
            usuarios = globales.getUsers()
            return len(usuarios[0])