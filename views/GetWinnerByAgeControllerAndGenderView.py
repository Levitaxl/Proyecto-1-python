from controllers.GetWinnerByAgeControllerAndGenderController import GetWinnerByAgeControllerAndGenderController

#Vista para obtener a los ganadores por grupo etario y genero


class GetWinnerByAgeControllerAndGenderView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):
        winners= GetWinnerByAgeControllerAndGenderController.invoke()

        if(winners==False):
            print('Recuerde cargar el archivo correctamente')
            return

        self.printWinner(self,winners['winnerJrF'],'Winner Jr F')
        self.printWinner(self,winners['winnerSeniorF'],'Winner Senior F')
        self.printWinner(self,winners['winnerMasterF'],'Winner Master F')
        self.printWinner(self,winners['winnerJrM'],'Female Winner M')
        self.printWinner(self,winners['winnerSeniorM'],'Male Winner M')
        self.printWinner(self,winners['winnerMasterM'],'Male Winner M')

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