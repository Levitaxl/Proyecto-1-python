from controllers.CountAllUsersController import CountAllUsersController

class CountAllUsersView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        countAllUsersController = CountAllUsersController()
        quantity= str(countAllUsersController.invoke())

        print(" ")
        print("There is in the system "+ quantity)
        print(" ")

        input('Press enter on the keyboard to exit: ')