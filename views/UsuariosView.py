
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
import platform
#Vista principal con todas las opciones de visualizacion en el sistema

class UsuariosView:

    menu_options= {
            1: 'Lista con la totalidad de participantes',
            2: 'Cantidad total de participantes',
            3: 'Cantidad de participantes por grupo etario ',
            4: 'Cantidad de participantes por gender',
            5: 'Ganadores por grupo etario',
            6: 'Ganadores por gender',
            7: 'Ganadores por grupo etario y gender',
            8: 'Ganador genera',
            9: 'Histograma de participante por grupo etario',
            0: 'salir'
        }

    def __init__(self):
       pass

       
    @classmethod
    def print_menu(self):
        print("")
        print('----------------------')
        for key in self.menu_options.keys():
            print (key, '--', self.menu_options[key] )

        print('----------------------')
        print("")
 
    def option1():
        GetAllUsersView.showMenu()
    
    def option2():
        CountAllUsersView.showMenu()
        
    def option3():
        CountAllUsersByAgeGroupView.showMenu()
        
    def option4():
        CountAllUsersByGenderView.showMenu()

    def option5():
        GetWinnerByAgeGroupView.showMenu()
        
    def option6():
        GetWinnerByGenderView.showMenu()
        
    def option7():
        GetWinnerByAgeControllerAndGenderView.showMenu()
        
    def option8():
        GetWinnerView.showMenu()

    def option9():
        HistogramView.showMenu()
        
    def option0():
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
                print('Ingrese un numero ...')
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
                print('Opcion Invalida. ')

    def clear_console():
        if platform.system()=='Windows':
            os.system('cls')
        else:
            os.system('clear')