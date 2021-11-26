from controllers.GetWinnerController import GetWinnerController
#Vista para obtener al ganador

class GetWinnerView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):
        winner= GetWinnerController.invoke()
        
        if(winner==False):
            print('Remember to upload the file')
            return

        self.printWinner(self,winner,'Winner')

        input('Press enter on the keyboard to exit: ')


    def printWinner(self,winner,header):
        print('---------------------------------------------')
        print('|'+header)
        print('|CI               | '+winner['ci'])
        print('|P.Apellido       | '+winner['primer_apellido'])
        print('|S.Apellido       | '+winner['segundo_apellido'])
        print('|Nombre           | '+winner['nombre'])
        print('|Inicial S.Nombre | '+winner['inicial_segundo_nombre'])
        print('|Sexo             | '+winner['sexo'])
        print('|Edad             | '+winner['edad'])
        print('|Horas            | '+winner['horas'])
        print('|Minutos          | '+winner['minutos'])
        print('|Segundos         | '+winner['segundos'])
        print('---------------------------------------------')