from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from Data.Render.Estructura import Estructura
from Data.Texturas.Texturas import Texturas
from kivy.lang.builder import Builder
from Data.Mapa.Mapa import Mapa


Builder.load_file("Data/KVventanas/Juego.kv")


class Juego(Screen):
    canvas_juego = ObjectProperty()

    def __init__(self,**kargs):
        Screen.__init__(self,**kargs)
        self.name = "Juego"
        self.estructura = Estructura()

    def test_map(self):
        mapa = self.mapa.get_mapa()
        

        

    def update(self,dt):
        self.estructura.update(dt)

    def draw(self,size,dt):
        self.estructura.draw(size, self.canvas_juego.canvas,dt)


