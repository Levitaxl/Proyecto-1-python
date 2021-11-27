from models.UsersModel import UsersModel

#Servicio con la logica de negocio, que se encarga de contar y separar a los ganadores en el sistema por grupo genero.

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
            gender= user['gender']
            if(gender =='F'):
                if((int(winner['hours']) >= int(user["hours"])) and (int(winner['minutes']) >= int(user["minutes"])) and (int(winner['seconds']) >= int(user["seconds"]))):
                    winner={
                        'hours' :    user['hours'],
                        'minutes' :  user["minutes"],
                        'seconds':   user["seconds"],
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
            age=int(user["age"])
            if(age>25 and  age<=40):
                 if((int(winner['hours']) >= int(user["hours"])) and (int(winner['minutes']) >= int(user["minutes"])) and (int(winner['seconds']) >= int(user["seconds"]))):
                    winner={
                        'hours' :    user['hours'],
                        'minutes' :  user["minutes"],
                        'seconds':   user["seconds"],
                        'idWinner' : i
                    }
            i=i+1
        return winner['idWinner']