import globales

class CountAllUsersByAgeGroupModel:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
            usuarios = globales.getUsers()
            return usuarios[0]
                