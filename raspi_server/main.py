from  utils.server_socket import ServerSocket
def main():
    server_socket = ServerSocket()
    print("[STARTING] server is starting...")
    server_socket.create_socket()
    server_socket.start()
    
if __name__ == "__main__":
    main()