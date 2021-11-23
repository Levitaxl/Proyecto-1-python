from models.UsersModel import UsersModel


class CountAllUsersByGenderService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        usersModel = UsersModel()
        users =  usersModel.invoke()
        qtyF =0
        qtyM =0
      
        for user in users:
            gender=user["sexo"]
            if(gender == 'F'):
                qtyF=qtyF+1
            elif(gender == 'M'):
                qtyM= qtyM+1

        response ={
            "qtyF":qtyF,
            "qtyM":qtyM
        }

        return (response)