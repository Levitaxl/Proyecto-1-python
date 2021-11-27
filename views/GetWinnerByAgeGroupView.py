from controllers.GetWinnerByAgeGroupController import GetWinnerByAgeGroupController


#Vista para obtener a los ganadores por grupo etario

class GetWinnerByAgeGroupView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        

        winners= GetWinnerByAgeGroupController.invoke()

        if(winners==False):
            print('Recuerde cargar el archivo correctamente')
            return

        self.printWinner(self,winners['winnerJr'],'Winner Jr')
        self.printWinner(self,winners['winnerSenior'],'Winner Senior')
        self.printWinner(self,winners['winnerMaster'],'Winner Master')

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