from controllers.GetWinnerController import GetWinnerController
#Vista para obtener al ganador

class GetWinnerView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):
        winner= GetWinnerController.invoke()
        
        if(winner==False):
            print('Recuerde cargar el archivo correctamente')
            return

        self.printWinner(self,winner,'Winner')

        input('Press enter on the keyboard to exit: ')


    def printWinner(self,winner,header):
        print('---------------------------------------------')
        print('|'+header)
        print('|CI               | '+winner['ci'])
        print('|P.Apellido       | '+winner['surname'])
        print('|S.Apellido       | '+winner['second_surname'])
        print('|Nombre           | '+winner['name'])
        print('|Inicial S.Nombre | '+winner['middle_initial'])
        print('|Sexo             | '+winner['gender'])
        print('|Edad             | '+winner['age'])
        print('|Horas            | '+winner['hours'])
        print('|Minutos          | '+winner['minutes'])
        print('|Segundos         | '+winner['seconds'])
        print('---------------------------------------------')