
from pathlib import Path
import globales
from models.LoadFileModel import LoadFileModel

#Servicio con la logica de negocio, que se encarga de validar la ruta, y cargar los usuarios en el sistema.
class AddANewRouteService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self,fileName):
        fileObj = Path(fileName)
        response= fileObj.is_file()
        if(response):
            globales.setRuta(fileName)
            list=LoadFileModel.invoke(fileName)
            if(list):
                globales.appendUser(list) 
            else :
                response = False
        return (response)
