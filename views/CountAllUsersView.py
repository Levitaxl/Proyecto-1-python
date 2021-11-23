from controllers.CountAllUsersController import CountAllUsersController

class CountAllUsersView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        countAllUsersController = CountAllUsersController()
        quantity= str(countAllUsersController.invoke())

        print("Hay en el sistema "+quantity)


        input('Apriete enter para salir: ')
