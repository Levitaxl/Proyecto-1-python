from services.CountAllUsersByAgeGroupService import CountAllUsersByAgeGroupService

class CountAllUsersByAgeGroupController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        getAllUsersServiceByAgeGroup = CountAllUsersByAgeGroupService()
        quantity = getAllUsersServiceByAgeGroup.invoke()
        return quantity