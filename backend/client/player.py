import socket


class Player :

    def __init__(self):
        self.port = 5050
        self.server = socket.gethostbyname(socket.gethostname())
        self.addr = (self.server , self.port)
        self.format = "utf-8"
        self.HEADER = 128



    def receive_msg(self):
        pass


    def send_msg(self):
        pass

    def connect_to_server(self):
        client = socket.socket(socket.AF_INET ,socket.SOCK_STREAM)