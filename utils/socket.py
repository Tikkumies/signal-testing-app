import socket

class ClientSocket:
    def __init__(self):
        self.header =  64
        self.port = 5050
        self.format = 'utf-8'
        self.disconnect_message = "!DISCONNECT"
        self.server = ""
        self.addr = (self.server, self.port)
    def connect(self):
        try:
            self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client.connect(self.addr)
        except:
            print("Failed to conncect")

    def disconnect(self):
        self.client.close()

    def send(self, msg):
        try:
            message = msg.encode(self.format)
            msg_length = len(message)
            send_length = str(msg_length).encode(self.format)
            send_length += b' ' * (self.header - len(send_length))
            self.client.send(send_length)
            self.client.send(message)
            print(self.client.recv(2048).decode(self.format))
        except:
            self.disconnect()
