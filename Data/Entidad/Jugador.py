
from Data.Entidad.Entidad import Entidad

class Jugador(Entidad):
    
    def __init__(self, nombre, pos):
        super().__init__(pos)
        
        self.nombre = nombre
        
        
        
    def update(self,dt):
        pass
    
    
    def draw(self,dt):
        pass
        
        