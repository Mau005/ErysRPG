from Data.Core.Constantes import RANGO_X_OBJS, RANGO_Y_OBJS
from Data.Mapa.Mapa import Mapa
from Data.Objetos.Lista_Objetos import Lista_Objetos


class Estructura:

    def __init__(self, tools):
        """
        Clase Orientada a poder organizar el orden de dibujado de los objetos,
        para darle una profundidad indicando el nivel de la capa de un solo piso
        """
        self.__capas = {1: [], 2: [], 3: [], 4: [], "coll1": [], "coll2": [], "objs": []}
        # Problema de renderizado, posiblemente se clone el objeto, y est eobjeto se vuelva pesado con el tiempo
        # usando mas memoria RAM de la que requiera un objeto unico
        
        self.Lista_Objetos = Lista_Objetos()
        self.size = [32,32]
        self.mapa = Mapa(10,10)
        self.mapa.gen_mapa() # genera un pequeño mapaa automaticamente
        self.puntos = [0,0]
        self.tools = tools
        
        self.__updateSize()
        self.registrar_canvas()


    def registrarProvisorio(self,obj):
        """
        Methodo creado para realizar pruebas
        :param capa: es el id, de la posicion de dibujado
        :param obj: es el objeto, que sera renderizado
        :return: None
        """
        self.__capas[obj.get_capa_dibujado()].append(obj)
        self.__capas["objs"] = obj


    def registrar(self, capa, obj):
        """
        Agrega objetos a los niveles de capa, para renderizar el mapa
        :param capa: capa nesesaria entre 1 añ 4
        :param obj: objetos multiples que necesitan que se muestren en pantalla
        :return: void
        """
        self.__capas[capa].append(obj)

    def actualizarColl(self,jugador):
        resultado = {}
        for objetos in self.__capas["coll1"]:
            pass
        for objetos in self.__capas["coll2"]:
            pass
        
    def __updateSize(self):
        size = self.tools["size"]
        self.size = [size[0]/RANGO_X_OBJS,size[1]/RANGO_Y_OBJS] #methodo que define el tamaño de los cuadros en el juego

    def update(self,  dt):
        """methodo update que ajusta todo

        Args:
            dt (_type_): el tiempo transcurrido
        """
        self.__updateSize()
        
        
    def __orden_de_objetos(self):
        """Ordena los objetos en capas, para su renderizado previo
        """
        for elementos in self.__capas["objs"]:
            self.__capas[elementos.get_capa_dibujado()].append(elementos)
    
    def registrar_canvas(self):
        """Registra a los objetos en una lista, estos objetos seran asignado para su renderizado
        """
        mapa = self.mapa.get_mapa()
        for x in range(len(mapa)):
            for y in range(len(mapa[x])):
                idObjs = mapa[x][y]
                if idObjs >= 1:
                    print(self.size)
                    self.__capas["objs"].append(self.Lista_Objetos.get_objeto(idObjs,[x*self.size[0],y*self.size[1]]))
        self.__orden_de_objetos()
        
        

    def draw(self, canvas,dt):
        """
        Dibuja solo las capas enumeradas previamentes
        :param canvas: lienzo donde se dibujaran los objetos
        :return: None
        """
        
        canvas.clear() #limpiamos el canvas para dibujar
        for capas in range(1,5):
            for objetos in self.__capas[capas]:
                canvas.add(objetos)
                
        