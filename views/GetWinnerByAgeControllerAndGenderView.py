from controllers.GetWinnerByAgeControllerAndGenderController import GetWinnerByAgeControllerAndGenderController

class GetWinnerByAgeControllerAndGenderView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):
        winners= GetWinnerByAgeControllerAndGenderController.invoke()
        self.printWinner(self,winners['winnerJr'],'Winner Jr')
        self.printWinner(self,winners['winnerSenior'],'Winner Senior')
        self.printWinner(self,winners['winnerMaster'],'Winner Master')
        self.printWinner(self,winners['winnerF'],'Female Winner')
        self.printWinner(self,winners['winnerM'],'Male Winner')

        input('Apriete enter para salir: ')
        
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