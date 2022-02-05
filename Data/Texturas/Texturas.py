from kivy.graphics import Rectangle
from Data.Entidad.Entidad import Entidad


class Texturas(Rectangle):

    def __init__(self, nivelCapa, ruta_textura, pos, **kargs):
        Rectangle.__init__(self, **kargs)
        self.__nivelCapa = nivelCapa
        self.source = ruta_textura
        self.pos_mapa = Entidad(pos)
        self.pos = pos

    def get_capa_dibujado(self):
        return self.__nivelCapa
    
    def draw(self, size, dt):
        self.size = size

    def update(self, dt):
        pass
        
