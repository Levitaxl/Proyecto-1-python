from models.UsersModel import UsersModel

#Servicio con la logica de negocio, que se encarga de obtener al ganador en el sistema.
class GetWinnerService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        users =  UsersModel.invoke()
        if (users==False):
            return False
        idWinner      =   self.winner(self,users) 

        winner = users[idWinner],
        
        return winner[0]

    def winner(self,users):
        winner={
            'hours' :    9999999,
            'minutes' :  9999999,
            'seconds':   9999999,
            'idWinner' : -1
        }
        i=0
        for user in users:
            if((int(winner['hours']) >= int(user["hours"])) and (int(winner['minutes']) >= int(user["minutes"])) and (int(winner['seconds']) >= int(user["seconds"]))):
                winner={
                    'hours' :    user['hours'],
                    'minutes' :  user["minutes"],
                    'seconds':   user["seconds"],
                    'idWinner' : i
                }
            i=i+1
        return winner['idWinner']