import socket 
import threading
from utils.get_ip import parse_wlan_from_ifconfig, get_network_adapters
from utils.gpio import control_relays

HEADER = 64
PORT = 5050
SERVER = parse_wlan_from_ifconfig(get_network_adapters())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

class ServerSocket:
    def create_socket(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(ADDR)

    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")

        connected = True
        while connected:
            try:
                msg_length = conn.recv(HEADER).decode(FORMAT)
                if msg_length:
                    msg_length = int(msg_length)
                    msg = conn.recv(msg_length).decode(FORMAT)
                    if msg == DISCONNECT_MESSAGE:
                        connected = False

                    print(f"[{addr}] {msg}")
                    conn.send("Msg received".encode(FORMAT))
                    control_relays(msg)
            except:
                conn.close()
                connected = False
                print("Conncection closed")    
        conn.close()
            
    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on {SERVER}")
        while True:
            conn, addr = self.server.accept()
            thread = threading.Thread(target=self.handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
