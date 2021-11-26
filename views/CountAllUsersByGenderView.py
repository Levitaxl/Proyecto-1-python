from controllers.CountAllUsersByGenderController import CountAllUsersByGenderController

class CountAllUsersByGenderView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):
        quantity= CountAllUsersByGenderController.invoke()

        females ="|Females "+str(quantity['qtyF'])+"|"
        males   ="|Males "+str(quantity['qtyM'])+"|"
        
        print(" ")
        print(females+" "+males)
        print(" ")

        input('Press enter on the keyboard to exit: ')
