class LoadFileModel:
    def __init__(self):
        pass

    @classmethod
    def invoke(self,fileName):
        archivo = open(fileName)
        list=[]
        try:
            for linea in archivo:
                data=linea.split(",")
                diccionario={
                    'ci': data[0].strip(),
                    'surname': data[1].strip(),
                    'second_surname': data[2].strip(),
                    'name': data[3].strip(),
                    'middle_initial': data[4].strip(),
                    'gender': data[5].strip(),
                    'age': data[6].strip(),
                    'hours': data[7].strip(),
                    'minutes': data[8].strip(),
                    'seconds': data[9].strip(),
                }
                list.append(diccionario)
        except:
            list=False

        return list