from controllers.CountAllUsersByAgeGroupController import CountAllUsersByAgeGroupController

class CountAllUsersByAgeGroupView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):
        usersQuantity= CountAllUsersByAgeGroupController.invoke()

        juniors="|Juniors:"+str(usersQuantity['qtyJuniors'])+"|"
        seniors="|Seniors:"+str(usersQuantity['qtySeniors'])+"|"
        masters="|Masters:"+str(usersQuantity['qtyMasters'])+"|"
        print(" ")
        print(juniors+" "+seniors+" "+masters)
        print(" ")


        input('Press enter on the keyboard to exit: ')
