from controllers.GetWinnerController import GetWinnerController

class GetWinnerView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        countAllUsersController = GetWinnerController()
        winner= countAllUsersController.invoke()

        print(winner)


        input('Apriete enter para salir: ')
