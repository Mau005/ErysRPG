from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty

from Data.Render.Estructura import Estructura
from Data.Texturas.Texturas import Texturas
from kivy.lang.builder import Builder
from Data.Mapa.Mapa import Mapa


Builder.load_file("Data/KVventanas/Juego.kv")


class Juego(Screen):
    canvas_juego = ObjectProperty()

    def __init__(self,tools, **kargs):
        Screen.__init__(self,**kargs)
        self.name = "Juego"
        self.tools = tools
        self.estructura = Estructura(self.tools)

    def test_map(self):
        mapa = self.mapa.get_mapa()
        

        

    def update(self,dt):
        self.estructura.update(dt)

    def draw(self,dt):
        self.estructura.draw(self.canvas_juego.canvas,dt)


