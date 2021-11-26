from controllers.GetWinnerByGenderController import GetWinnerByGenderController

class GetWinnerByGenderView:
    def __init__(self):
       pass

    @classmethod    
    def showMenu(self):

        winners= GetWinnerByGenderController.invoke()

        
        self.printWinner(self,winners['winnerF'],'Female Winner')
        self.printWinner(self,winners['winnerM'],'Male Winner')

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