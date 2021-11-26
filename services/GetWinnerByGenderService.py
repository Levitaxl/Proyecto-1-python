from models.UsersModel import UsersModel


class GetWinnerByGenderService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        users =  UsersModel.invoke()
        
        if(users==False):
            return False
        
        idWinnerF      =   self.winnerF(self,users) 
        idWinnerM  =       self.winnerM(self,users) 

        winners = {
            'winnerF'       : users[idWinnerF],
            'winnerM'       : users[idWinnerM],
        }
        return (winners)

    def winnerF(self,users):
        winner={
            'hours' :    9999999,
            'minutes' :  9999999,
            'seconds':   9999999,
            'idWinner' : -1
        }
        i=0
        for user in users:
            gender= user["sexo"]
            if(gender =='F'):
                if((int(winner['hours']) >= int(user['horas'])) and (int(winner['minutes']) >= int(user['minutos'])) and (int(winner['seconds']) >= int(user['segundos']))):
                    winner={
                        'hours' :    user['horas'],
                        'minutes' :  user['minutos'],
                        'seconds':   user['segundos'],
                        'idWinner' : i
                    }
            i=i+1
        return winner['idWinner']
    
    def winnerM(self,users):
        winner={
            'hours' :    9999999,
            'minutes' :  9999999,
            'seconds':   9999999,
            'idWinner' : -1
        }
        i=0
        for user in users:
            age=int(user["edad"])
            if(age>25 and  age<40):
                 if((int(winner['hours']) >= int(user['horas'])) and (int(winner['minutes']) >= int(user['minutos'])) and (int(winner['seconds']) >= int(user['segundos']))):
                    winner={
                        'hours' :    user['horas'],
                        'minutes' :  user['minutos'],
                        'seconds':   user['segundos'],
                        'idWinner' : i
                    }
            i=i+1
        return winner['idWinner']