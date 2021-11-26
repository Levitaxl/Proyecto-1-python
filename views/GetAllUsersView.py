from controllers.GetAllUsersController import GetAllUsersController

#Vista para listar a todos los usuarios en el sistema


class GetAllUsersView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):
        
        users= GetAllUsersController.invoke()
        if(users==False):
            print('Remember to upload the file')
            return

             
        header=['CI','P.Apellido','S.Apellido','Nombre',' Inicial S.Nombre','Sexo','Edad','Horas','Minutos','Segundos']
     
        print("{: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15}".format(*header))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for user in users:
            userInfo= user.values()
            print("{: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15}".format(*userInfo))

        input('Press enter on the keyboard to exit: ')