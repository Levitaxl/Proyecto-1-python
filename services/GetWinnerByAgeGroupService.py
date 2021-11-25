from models.UsersModel import UsersModel


class GetWinnerByAgeGroupService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        usersModel = UsersModel()
        users =  usersModel.invoke()
        idWinnerJr =self.calculate(self,users) 
        print(users[idWinnerJr])
        print(idWinnerJr)
        return (idWinnerJr)

    def calculate(self,users):
        idWinner=-1
        winner={
            'hours' :    0,
            'minutes' :  0,
            'seconds':   0,
            'idWinner' : -1
        }
        i=0
        for user in users:
            age=int(user["edad"])
            if(age<= 25):
                if(idWinner==-1):
                    winner={
                        'hours' :    int(user['horas']),
                        'minutes' :  int(user['minutos']),
                        'seconds':   int(user['segundos']),
                        'idWinner' : i
                    }
                elif((winner['hours']<- int(user['horas'])) and (winner['minutes']<- int(user['minutos'])) and (winner['seconds']<-int(user['segundos']))):
                    winner={
                        'hours' :    user['horas'],
                        'minutes' :  user['minutos'],
                        'seconds':   user['segundos'],
                        'idWinner' : i
                    }
            i=i+1
        return winner['idWinner']