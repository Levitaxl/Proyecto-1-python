from models.UsersModel import UsersModel

#Servicio con la logica de negocio, que se encarga de contar y separar a los usuarios en el sistema por grupo genero.

class CountAllUsersByGenderService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        users =  UsersModel.invoke()
        if(users==False):
            return False
        qtyF =0
        qtyM =0
      
        for user in users:
            gender=user["gender"]
            if(gender == 'F'):
                qtyF=qtyF+1
            elif(gender == 'M'):
                qtyM= qtyM+1

        response ={
            "qtyF":qtyF,
            "qtyM":qtyM
        }

        return (response)