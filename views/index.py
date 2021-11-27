import views.ArchivoView
import views.UsuariosView
#Vista del menu principal del sistema, al entrar en el

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
        archivoView = views.ArchivoView.ArchivoView
        archivoView.showMenu()
        
 
    def option2():
        usuariosView = views.UsuariosView.UsuariosView
        usuariosView.showMenu()
        

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
                print('Thanks message before exiting')
                exit()
            else:
                print('Opcion Invalida. ')