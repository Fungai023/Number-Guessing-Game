import socket
import threading

class Server:

    def __init__(self , server , port):
        self.port = port
        self.server = server
        port = 5050
        server = socket.gethostbyname(socket.gethostname())
        self.addr = (server , port)
        self.format = "utf-8"
        self.HEADER = 128

    def client_handler(self , connection , address):
        print(f"[NEW CONNECTION] form {address}")
        connected = True
        while connected :
            message_length = connection.recv(self.HEADER).decode(self.format)
            if message_length != 0 :
                msg_length = int(message_length)
                message = connection.recv(self.HEADER).decode(self.format)
                if not connected:
                    break
            print(f"[MESSAGE] {address} : {message}")

        connection.close()

    def receive_msg(self):
        pass


    def send_msg(self):
        pass

    def start(self):
        server_conn =  socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        server_conn.bind(self.addr)
        server_conn.listen()
        while True :
            conn , address = server_conn.accept()
            thread = threading.Thread(target= self.client_handler , args= (conn , address) )
            thread.start()
            print(f"ACTIVE CONNECTIONS :  {threading.active_count()-1}")

