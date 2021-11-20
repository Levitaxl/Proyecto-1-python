
from pathlib import Path
import globales
from models.LoadFileModel import LoadFileModel


class AddANewRouteService:
    def __init__(self):
        pass

    @classmethod
    def invoke(self,fileName):
        fileObj = Path(fileName)
        response= fileObj.is_file()
        if(response):
            globales.setRuta(fileName)
            loadFileModel= LoadFileModel()
            list=loadFileModel.invoke(fileName)
            globales.appendUser(list) 
        return (response)
