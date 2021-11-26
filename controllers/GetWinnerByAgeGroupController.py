from services.GetWinnerByAgeGroupService import GetWinnerByAgeGroupService

#Clase la que se encarga de gestionar de los servicios de obtener a los ganadores por grupo etario.
class GetWinnerByAgeGroupController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        users = GetWinnerByAgeGroupService.invoke()
        return users