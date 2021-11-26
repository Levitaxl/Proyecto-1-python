from models.UsersModel import UsersModel


class CountAllUsersByAgeGroupService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self):
        users =  UsersModel.invoke()
        if(users==False):
            return False
        qtyJuniors =0
        qtySeniors =0
        qtyMasters =0
        
      
        for user in users:
            age=int(user["edad"])
            if(age<= 25):
                qtyJuniors=qtyJuniors+1
            elif(age>25 and  age<40):
                qtySeniors= qtySeniors+1
            else:
                qtyMasters=qtyMasters+1

        response ={
                "qtyJuniors":qtyJuniors,
                "qtySeniors":qtySeniors,
                "qtyMasters":qtyMasters,
        }

        
        return (response)