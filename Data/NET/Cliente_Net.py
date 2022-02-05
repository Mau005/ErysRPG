from threading import Thread

class Cliente_Net(Thread):

    def __init__(self,ctl,addr):
        Thread.__init__(self)
        self.__ctl = ctl
        self.__addr = addr

    def run(self):
        Thread.run(self)


