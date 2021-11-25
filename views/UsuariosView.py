
import views.GetAllUsersView
import views.CountAllUsersView
import views.CountAllUsersByAgeGroupView
import views.CountAllUsersByGenderView
import views.GetWinnerByAgeView
import views.GetWinnerByGenderView
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
        getAllUsersView = views.GetAllUsersView.GetAllUsersView
        getAllUsersView.showMenu()
    
    def option2():
        clear = lambda: os.system('cls')
        clear()
        countAllUsersView = views.CountAllUsersView.CountAllUsersView
        countAllUsersView.showMenu()
    
    def option3():
        clear = lambda: os.system('cls')
        clear()
        countAllUsersView = views.CountAllUsersByAgeGroupView.CountAllUsersByAgeGroupView
        countAllUsersView.showMenu()

    def option4():
        clear = lambda: os.system('cls')
        clear()
        countAllUsersView = views.CountAllUsersByGenderView.CountAllUsersByGenderView
        countAllUsersView.showMenu()

    def option5():
        clear = lambda: os.system('cls')
        clear()
        countAllUsersView = views.GetWinnerByAgeView.GetWinnerByAgeView
        countAllUsersView.showMenu()
    
    def option6():
        clear = lambda: os.system('cls')
        clear()
        countAllUsersView = views.GetWinnerByGenderView.GetWinnerByGenderView
        countAllUsersView.showMenu()

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
                self.option1()
            elif option == 8:
                self.option1()
            elif option == 9:
                self.option1()
            elif option == 0:
                self.option0()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')