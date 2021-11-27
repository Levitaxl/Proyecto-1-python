from models.UsersModel import UsersModel

#Servicio con la logica de negocio, que se encarga de contar y separar a los ganadores en el sistema por grupo etario.
class GetWinnerByAgeControllerAndGenderService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        users =  UsersModel.invoke()
        if(users==False):
            return False
        idWinnerJrF      =   self.winnerJunior(self,users,'F') 
        idWinnerSeniorF  =   self.winnerSenior(self,users,'F') 
        idWinnerMasterF  =   self.winnerMaster(self,users,'F') 
        idWinnerJrM      =   self.winnerJunior(self,users,'M') 
        idWinnerSeniorM  =   self.winnerSenior(self,users,'M') 
        idWinnerMasterM  =   self.winnerMaster(self,users,'M') 

        winners = {
            'winnerJrF'      : users[idWinnerJrF],
            'winnerSeniorF'  : users[idWinnerSeniorF],
            'winnerMasterF'  : users[idWinnerMasterF],
            'winnerJrM'      : users[idWinnerJrM],
            'winnerSeniorM'  : users[idWinnerSeniorM],
            'winnerMasterM'  : users[idWinnerMasterM]
        }
        return (winners)

    def winnerJunior(self,users,gender):
        winner={
            'hours' :    9999999,
            'minutes' :  9999999,
            'seconds':   9999999,
            'idWinner' : -1
        }
        i=0
        for user in users:
            age=int(user["age"])
            if(age<= 25 and gender==user['gender']):
                if((int(winner['hours']) >= int(user["hours"])) and (int(winner['minutes']) >= int(user["minutes"])) and (int(winner['seconds']) >= int(user["seconds"]))):
                    winner={
                        'hours' :    user['hours'],
                        'minutes' :  user["minutes"],
                        'seconds':   user["seconds"],
                        'idWinner' : i
                    }
            i=i+1
        return winner['idWinner']
    
    def winnerSenior(self,users,gender):
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
            if(age>25 and  age<=40 and gender==user['gender']):
                 if((int(winner['hours']) >= int(user["hours"])) and (int(winner['minutes']) >= int(user["minutes"])) and (int(winner['seconds']) >= int(user["seconds"]))):
                    winner={
                        'hours' :    user['hours'],
                        'minutes' :  user["minutes"],
                        'seconds':   user["seconds"],
                        'idWinner' : i
                    }
            i=i+1
        return winner['idWinner']

    def winnerMaster(self,users,gender):
        idWinner=-1
        winner={
            'hours' :    9999999,
            'minutes' :  9999999,
            'seconds':   9999999,
            'idWinner' : -1
        }
        i=0
        for user in users:
            age=int(user["age"] )
            if(age>40 and gender==user['gender']):
                if((int(winner['hours']) >= int(user["hours"])) and (int(winner['minutes']) >= int(user["minutes"])) and (int(winner['seconds']) >= int(user["seconds"]))):
                    winner={
                        'hours' :    user['hours'],
                        'minutes' :  user["minutes"],
                        'seconds':   user["seconds"],
                        'idWinner' : i
                    }
            i=i+1
        return winner['idWinner']