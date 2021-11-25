from pathlib import Path
import globales
from models.LoadFileModel import LoadFileModel


class GetAllUsersModel:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        try:
         usuarios = globales.getUsers()
         return usuarios[0]
        except:
            print("Recuerde cargar el archivo")
            return None