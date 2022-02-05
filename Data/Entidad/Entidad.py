from Data.Core.loger_base import logger


class Entidad:
    
    def __init__(self,pos):
        self.set_pos(pos)
        
    def set_pos(self,pos):
        if isinstance(pos,list):
            if len(pos) == 3:
                self._pos = pos
        else:
            logger.warning(f"No se pudo asignar la posicion correcta pos: {pos}")
            self._pos = [0,0,0]
            
    def get_x(self):
        return self._pos[0]

    def get_y(self):
        return self._pos[1]
    
    def get_z(self):
        return self._pos[2]
        
    def set_x(self,x):
        self._pos[0] = x
    
    def set_y(self,y):
        self._pos[1] = y
    
    def set_z(self,z):
        self._pos[2] = z
        
        
