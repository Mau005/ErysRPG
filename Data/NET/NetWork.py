from socket import socket

class NetWork:

    def __init__(self):
        self.socket = socket()

    def conectar(self,addres,port):
        try:
            self.socket.connect((addres,port))
            return True
        except ConnectionRefusedError as error:
            print(ConnectionRefusedError)
            print("No se pudo conectar con el servidor")
            self.socket = None
            return False
        #self.socket.connect_ex((addres,port))

    def get_socket(self):
        return self.socket

    def cerrar(self):
        self.socket.close()

    def enviar(self,data):
        self.socket.send(data)

    def recibir(self):
        self.socket.recv(1024)


if __name__ == "__main__":
    net = NetWork()
    net.conectar("localhost",7171)