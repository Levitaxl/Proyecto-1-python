class LoadFileModel:
    def __init__(self):
        pass

    @classmethod
    def invoke(self,fileName):
        archivo = open(fileName)
        list=[]
        for linea in archivo:
            data=linea.split(",")
            diccionario={
                'ci': data[0].strip(),
                'primer_apellido': data[1].strip(),
                'segundo_apellido': data[2].strip(),
                'nombre': data[3].strip(),
                'inicial_segundo_nombre': data[4].strip(),
                'sexo': data[5].strip(),
                'edad': data[6].strip(),
                'horas': data[7].strip(),
                'minutos': data[8].strip(),
                'segundos': data[9].strip(),
            }
            list.append(diccionario)
        return list