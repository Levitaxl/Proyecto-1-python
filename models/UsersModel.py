import globales

class UsersModel:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):

        try:
            usuarios = globales.getUsers()
            response = usuarios[0]
        except:
            response=False
            return response