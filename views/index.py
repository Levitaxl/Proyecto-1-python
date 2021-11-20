from views.ArchivoView import ArchivoView
import os
import globales
class IndexView:

    menu_options= {
            1: 'Archivo',
            2: 'Acciones',
            3: 'Exit'
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
        archivoView = ArchivoView()
        archivoView.showMenu()

 
    def option2():
        print('Handle option \'Acciones\'')


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
                print('Thanks message before exiting')
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 4.')