from controllers.GetWinnerByAgeController import GetWinnerByAgeController

class GetWinnerByAgeView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        countAllUsersController = GetWinnerByAgeController()
        quantity= str(countAllUsersController.invoke())

        print("El ganador jr es "+quantity)


        input('Apriete enter para salir: ')
