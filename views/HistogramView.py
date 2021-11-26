from controllers.CountAllUsersByAgeGroupController import CountAllUsersByAgeGroupController

class HistogramView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):
        quantity= CountAllUsersByAgeGroupController.invoke()
        
        if(quantity==False):
            print('Remember to upload the file')
            return
            
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

        input('Press enter on the keyboard to exit: ')
