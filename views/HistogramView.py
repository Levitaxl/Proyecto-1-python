from controllers.CountAllUsersByAgeGroupController import CountAllUsersByAgeGroupController

class HistogramView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):
        quantity= CountAllUsersByAgeGroupController.invoke()
        juniors=''
        senior=''
        master=''
        for i in range(quantity['qtyJuniors']):
            juniors=juniors+'*'
        for j in range(quantity['qtySeniors']):
            senior=senior+'*'
        for k in range(quantity['qtyMasters']):
            master=master+'*'

        print("Juniors ("+str(quantity['qtyJuniors'])+") "+juniors )
        print("Seniors ("+str(quantity['qtySeniors'])+") "+senior)
        print("Master  ("+str(quantity['qtyMasters'])+") "+master)


        input('Apriete enter para salir: ')
