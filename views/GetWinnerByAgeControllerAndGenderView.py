from controllers.GetWinnerByAgeControllerAndGenderController import GetWinnerByAgeControllerAndGenderController

class GetWinnerByAgeControllerAndGenderView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        getWinnerByAgeControllerAndGenderController = GetWinnerByAgeControllerAndGenderController()
        winners= getWinnerByAgeControllerAndGenderController.invoke()

        print(winners)


        input('Apriete enter para salir: ')
