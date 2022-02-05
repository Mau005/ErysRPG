from socket import socket


class Servidor:

    def __init__(self):
        self.socket = socket()
        self.socket.bind(("localhost",7171))
        self.socket.listen(0)


    def iniciar(self):
        while True:
            print(f"Servidor Iniciado")
            clt, addr = self.socket.accept()
            print(f"Cliente: {clt}, Addr: {addr}")

    def cerrar_servidor(self):
        self.socket.close()


if __name__ == "__main__":
    servidor = Servidor()
    servidor.iniciar()
    servidor.cerrar_servidor()