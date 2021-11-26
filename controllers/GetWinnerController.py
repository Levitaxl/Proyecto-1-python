from services.GetWinnerService import GetWinnerService

class GetWinnerController:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        user = GetWinnerService.invoke()
        return user