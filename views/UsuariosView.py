
from views.GetAllUsersView import GetAllUsersView
from views.CountAllUsersView import CountAllUsersView
from  views.CountAllUsersByAgeGroupView import CountAllUsersByAgeGroupView
from views.CountAllUsersByGenderView  import CountAllUsersByGenderView
from  views.GetWinnerByAgeGroupView import GetWinnerByAgeGroupView
from  views.GetWinnerByGenderView import GetWinnerByGenderView
from views.GetWinnerByAgeControllerAndGenderView import GetWinnerByAgeControllerAndGenderView
from  views.GetWinnerView import GetWinnerView
from  views.HistogramView import HistogramView
import views.index
import os

class UsuariosView:

    menu_options= {
            1: 'Lista con la totalidad de participantes',
            2: 'Cantidad total de participantes',
            3: 'Cantidad de participantes por grupo etario ',
            4: 'Cantidad de participantes por sexo',
            5: 'Ganadores por grupo etario',
            6: 'Ganadores por sexo',
            7: 'Ganadores por grupo etario y sexo',
            8: 'Ganador genera',
            9: 'Histograma de participante por grupo etario',
            0: 'salir'
        }

    def __init__(self):
       pass

       
    @classmethod
    def print_menu(self):
        for key in self.menu_options.keys():
            print (key, '--', self.menu_options[key] )

 
    def option1():
        clear = lambda: os.system('cls')
        clear()
        GetAllUsersView.showMenu()
    
    def option2():
        clear = lambda: os.system('cls')
        clear()
        CountAllUsersView.showMenu()
    
    def option3():
        clear = lambda: os.system('cls')
        clear()
        CountAllUsersByAgeGroupView.showMenu()

    def option4():
        clear = lambda: os.system('cls')
        clear()
        CountAllUsersByGenderView.showMenu()

    def option5():
        clear = lambda: os.system('cls')
        clear()
        GetWinnerByAgeGroupView.showMenu()
    
    def option6():
        clear = lambda: os.system('cls')
        clear()
        GetWinnerByGenderView.showMenu()
    def option7():
        clear = lambda: os.system('cls')
        clear()
        GetWinnerByAgeControllerAndGenderView.showMenu()
    def option8():
        clear = lambda: os.system('cls')
        clear()
        GetWinnerView.showMenu()
    def option9():
        clear = lambda: os.system('cls')
        clear()
        HistogramView.showMenu()

    def option0():
        clear = lambda: os.system('cls')
        clear()
        index = views.index.IndexView
        index.showMenu()

    @classmethod    
    def showMenu(self):
        while(True):
            self.print_menu()
            option = ''
            try:
                option = int(input('Enter your choice: '))
            except:
                print('Wrong input. Please enter a number ...')
            #Check what choice was entered and act accordingly
            if option == 1:
               self.option1()
            elif option == 2:
                self.option2()
            elif option == 3:
                self.option3()
            elif option == 4:
                self.option4()
            elif option == 5:
                self.option5()
            elif option == 6:
                self.option6()
            elif option == 7:
                self.option7()
            elif option == 8:
                self.option8()
            elif option == 9:
                self.option9()
            elif option == 0:
                self.option0()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')