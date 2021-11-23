from controllers.GetAllUsersController import GetAllUsersController
class GetAllUsersView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        getAllUsersController = GetAllUsersController()
        users= getAllUsersController.invoke()

        header=['CI','P.Apellido','S.Apellido','Nombre',' Inicial S.Nombre','Sexo','Edad','Horas','Minutos','Segundos']
     
        print("{: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15}".format(*header))
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
        for user in users:
            userInfo= user.values()
            print("{: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15} {: >15}".format(*userInfo))


        input('Apriete enter para salir: ')

        