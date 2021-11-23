from services.CountAllUsersByGenderService import CountAllUsersByGenderService

class CountAllUsersByGenderController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        getAllUsersServiceByGender = CountAllUsersByGenderService()
        quantity = getAllUsersServiceByGender.invoke()
        return quantity