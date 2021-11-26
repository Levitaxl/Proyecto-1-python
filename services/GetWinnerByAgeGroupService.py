from models.UsersModel import UsersModel


class GetWinnerByAgeGroupService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        usersModel = UsersModel()
        users =  usersModel.invoke()
        idWinnerJr      =   self.winnerJunior(self,users) 
        idWinnerSenior  =   self.winnerSenior(self,users) 
        idWinnerMaster  =   self.winnerMaster(self,users) 
        winners = {
            'winnerJr'      : users[idWinnerJr],
            'winnerSenior'  :users[idWinnerSenior],
            'winnerMaster'  : users[idWinnerMaster]
        }
        return (winners)

    def winnerJunior(self,users):
        winner={
            'hours' :    9999999,
            'minutes' :  9999999,
            'seconds':   9999999,
            'idWinner' : -1
        }
        i=0
        for user in users:
            age=int(user["edad"])
            if(age<= 25):
                if((int(winner['hours']) >= int(user['horas'])) and (int(winner['minutes']) >= int(user['minutos'])) and (int(winner['seconds']) >= int(user['segundos']))):
                    winner={
                        'hours' :    user['horas'],
                        'minutes' :  user['minutos'],
                        'seconds':   user['segundos'],
                        'idWinner' : i
                    }
            i=i+1
        return winner['idWinner']
    
    def winnerSenior(self,users):
        idWinner=-1
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

    def winnerMaster(self,users):
        idWinner=-1
        winner={
            'hours' :    9999999,
            'minutes' :  9999999,
            'seconds':   9999999,
            'idWinner' : -1
        }
        i=0
        for user in users:
            age=int(user["edad"])
            if(age>=40):
                if((int(winner['hours']) >= int(user['horas'])) and (int(winner['minutes']) >= int(user['minutos'])) and (int(winner['seconds']) >= int(user['segundos']))):
                    winner={
                        'hours' :    user['horas'],
                        'minutes' :  user['minutos'],
                        'seconds':   user['segundos'],
                        'idWinner' : i
                    }
            i=i+1
        return winner['idWinner']