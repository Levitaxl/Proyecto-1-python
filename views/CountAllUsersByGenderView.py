from controllers.CountAllUsersByGenderController import CountAllUsersByGenderController
#Vista para saber la cantidad de usuarios por genero

class CountAllUsersByGenderView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):
        quantity= CountAllUsersByGenderController.invoke()
        if(quantity==False):
            print('Remember to upload the file')
            return

        females ="|Females "+str(quantity['qtyF'])+"|"
        males   ="|Males "+str(quantity['qtyM'])+"|"
        
        print(" ")
        print(females+" "+males)
        print(" ")

        input('Press enter on the keyboard to exit: ')
