from controllers.GetWinnerByAgeController import GetWinnerByAgeController

class GetWinnerByAgeView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        countAllUsersController = GetWinnerByAgeController()
        winners= countAllUsersController.invoke()

        print(winners)


        input('Apriete enter para salir: ')
