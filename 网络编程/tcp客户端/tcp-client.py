import socket

def main():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.STREAM)

    server_ip = input('ip')

    server_port = input('port')

    tcp_client_socket.connect((server_ip, server_port))

    send_data = input('信息')

    tcp_client_socket.send(send_data.encode('utf-8'))

    recv_data = tcp_client_socket.recv(1024)

    print(recv_data.decode('gbk'))

    tcp_client_socket.close()
    
def __name__ == "__main__":
    main()