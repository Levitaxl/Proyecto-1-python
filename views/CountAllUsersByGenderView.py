from controllers.CountAllUsersByGenderController import CountAllUsersByGenderController

class CountAllUsersByGenderView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        countAllUsersController = CountAllUsersByGenderController()
        quantity= countAllUsersController.invoke()
        
        print("Hay en el sistema F "+str(quantity['qtyF']))
        print("Hay en el sistema M "+str(quantity['qtyM']))


        input('Apriete enter para salir: ')
