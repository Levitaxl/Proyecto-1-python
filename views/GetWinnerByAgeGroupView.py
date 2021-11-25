from controllers.GetWinnerByAgeGroupController import GetWinnerByAgeGroupController

class GetWinnerByAgeGroupView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        winners= GetWinnerByAgeGroupController.invoke()

        print(winners)


        input('Apriete enter para salir: ')
