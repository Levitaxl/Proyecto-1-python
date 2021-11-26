from services.CountAllUsersByAgeGroupService import CountAllUsersByAgeGroupService

class CountAllUsersByAgeGroupController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        quantity = CountAllUsersByAgeGroupService.invoke()
        return quantity