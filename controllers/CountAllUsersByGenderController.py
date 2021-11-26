from services.CountAllUsersByGenderService import CountAllUsersByGenderService

class CountAllUsersByGenderController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        quantity = CountAllUsersByGenderService.invoke()
        return quantity