from Data.Texturas.Texturas import Texturas

class Lista_Objetos:
    
    def __init__(self):
        
        self.__lista_objetos = {1:{"nivelCapa": 1, "ruta": "Assets/Suelos/2.png"}}
        
        
        
    def get_objeto(self,idObjeto,pos):
        obj = self.__lista_objetos[idObjeto]
        return Texturas(obj["nivelCapa"],obj["ruta"],pos)