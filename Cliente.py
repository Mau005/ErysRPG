import kivy

from Data.Juego import Juego

kivy.require("1.11.1")
from kivy.uix.screenmanager import ScreenManager
from kivy.app import App
from kivy.core.window import Window
from kivy.clock import Clock


class Cliente(App):

    def __init__(self, **kargs):
        App.__init__(self, **kargs)
        self.manejador = ScreenManager()
        self.juego = Juego()
        self.manejador.add_widget(self.juego)
        Clock.schedule_interval(self.update,1/60)
        Clock.schedule_interval(self.draw,1/60)
        
    def update(self,*dt):
        self.juego.update(dt)
        
    def draw(self,*dt):
        self.juego.draw(Window.size,dt)

    def build(self):
        return self.manejador


if __name__ == "__main__":
    cl = Cliente()
    cl.run()
