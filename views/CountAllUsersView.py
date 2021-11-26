from controllers.CountAllUsersController import CountAllUsersController

class CountAllUsersView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):


        quantity= str(CountAllUsersController.invoke())

        if(quantity==False):
            print('Remember to upload the file')
            return
        

        print(" ")
        print("There is in the system "+ quantity)
        print(" ")

        input('Press enter on the keyboard to exit: ')