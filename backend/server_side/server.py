import socket
import threading

class Server():
    port = 5050
    server = socket.gethostbyname(socket.gethostname())

    def __init__(self, port , server):
        self.port = port
        self.server = server
        self.addr = (server , port)

    def client_handler(self):
        pass

    def start(self):
        server_conn =  socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        server_conn.bind(self.addr)
        server_conn.listen()
        while True :
            conn , address = server_conn.accept()
            thread = threading.Thread(target= self.client_handler() , args= (conn , address) )
            thread.start()
            print(f"ACTIVE CONNECTIONS  {threading.active_count()}")