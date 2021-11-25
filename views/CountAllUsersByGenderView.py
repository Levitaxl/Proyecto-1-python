from controllers.CountAllUsersByGenderController import CountAllUsersByGenderController

class CountAllUsersByGenderView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):
        quantity= CountAllUsersByGenderController.invoke()

        females ="|Females "+str(quantity['qtyF'])+"|"
        males   ="|Males "+str(quantity['qtyM'])+"|"
        
        print(females+" "+males)


        input('Apriete enter para salir: ')
