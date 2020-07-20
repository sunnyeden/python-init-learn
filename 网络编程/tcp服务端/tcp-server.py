import socket

def main():
    tcp_server_socket = socket.socket(socket.AF_INET, socket.STREAM)
    tcp_server_socket.bind(('', 7890))
    tcp_server_socket.listen(128)

    while True:

        new_client_socket, client_addr = tcp_server_socket.accept()

        while True:

            recv_data = new_client_socket.recv(1024)
            print(recv_data.decode('utf-8'))

            if recv_data:
                new_client_socket.send('hello'.encode('utf-8'))
            else:
                break

        tcp_client_socket.close()

def __name__ == "__main__":
    main()