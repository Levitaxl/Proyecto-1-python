from controllers.CountAllUsersByAgeGroupController import CountAllUsersByAgeGroupController

class CountAllUsersByAgeGroupView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        countAllUsersController = CountAllUsersByAgeGroupController()
        quantity= countAllUsersController.invoke()
        print(quantity)

        print("Hay en el sistema Juniors "+str(quantity['qtyJuniors']))
        print("Hay en el sistema Seniors "+str(quantity['qtySeniors']))
        print("Hay en el sistema Master  "+str(quantity['qtyMasters']))


        input('Apriete enter para salir: ')
