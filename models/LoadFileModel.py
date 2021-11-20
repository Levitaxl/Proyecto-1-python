class LoadFileModel:
    def __init__(self):
        pass

    @classmethod
    def invoke(self,fileName):
        archivo = open(fileName)
        linea=archivo.readline().replace(" ","")
        for linea in archivo:
            print(linea)
            data= linea.split()
            print(data)
