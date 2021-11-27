from models.UsersModel import UsersModel

#Servicio con la logica de negocio, que se encarga de contar y separar a los ganadores en el sistema por grupo etario.
class GetWinnerByAgeGroupService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        users =  UsersModel.invoke()
        if(users==False):
            return False
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
            age=int(user["age"])
            if(age<= 25):
                if((int(winner['hours']) >= int(user['hours'])) and (int(winner['minutes']) >= int(user['minutes'])) and (int(winner['seconds']) >= int(user['seconds']))):
                    winner={
                        'hours' :    user['hours'],
                        'minutes' :  user['minutes'],
                        'seconds':   user['seconds'],
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
            age=int(user["age"])
            if(age>25 and  age<40):
                 if((int(winner['hours']) >= int(user['hours'])) and (int(winner['minutes']) >= int(user['minutes'])) and (int(winner['seconds']) >= int(user['seconds']))):
                    winner={
                        'hours' :    user['hours'],
                        'minutes' :  user['minutes'],
                        'seconds':   user['seconds'],
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
            age=int(user["age"])
            if(age>=40):
                if((int(winner['hours']) >= int(user['hours'])) and (int(winner['minutes']) >= int(user['minutes'])) and (int(winner['seconds']) >= int(user['seconds']))):
                    winner={
                        'hours' :    user['hours'],
                        'minutes' :  user['minutes'],
                        'seconds':   user['seconds'],
                        'idWinner' : i
                    }
            i=i+1
        return winner['idWinner']