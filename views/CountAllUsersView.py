from controllers.CountAllUsersController import CountAllUsersController

#Vista para saber la cantidad de usuarios en el sistema
class CountAllUsersView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):


        quantity= CountAllUsersController.invoke()

        if(quantity==False):
            print('Remember to upload the file')
            return
        
        quantity= str(CountAllUsersController.invoke())

        print(" ")
        print("There is in the system "+ quantity)
        print(" ")

        input('Press enter on the keyboard to exit: ')