class Mapa():

    def __init__(self, xMax, yMax):
        self.__mapa = self.asignarMapa(xMax, yMax)

    def gen_mapa(self):
        self.__mapa = [[1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        
        
    def get_pos(self,x,y):
        return self.__mapa[x][y]
    
    def get_mapa(self):
        return self.__mapa

    def asignarMapa(self, xMax, yMax):
        self.__xMax = xMax
        self.__yMax = yMax
        self._mapa = [[[] for y in range(self.__xMax)] for x in range(self.__yMax)]
