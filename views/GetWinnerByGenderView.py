from controllers.GetWinnerByGenderController import GetWinnerByGenderController

class GetWinnerByGenderView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        countAllUsersController = GetWinnerByGenderController()
        winners= countAllUsersController.invoke()

        print(winners)


        input('Apriete enter para salir: ')
