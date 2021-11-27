from controllers.GetWinnerByGenderController import GetWinnerByGenderController
#Vista para obtener a los ganadores por  genero

class GetWinnerByGenderView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        winners= GetWinnerByGenderController.invoke()
        if(winners==False):
            print('Recuerde cargar el archivo correctamente')
            return
        
        self.printWinner(self,winners['winnerF'],'Female Winner')
        self.printWinner(self,winners['winnerM'],'Male Winner')

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