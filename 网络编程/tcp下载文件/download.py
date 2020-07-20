import socket

def main():
    tcp_client_socket = socket.socket(socket.AF_INET, socket.STREAM)
    server_ip = input('ip')
    server_port = input('port')
    tcp_client_socket.connect((server_ip, server_port))

    download_file = input('请输入要下载的文件名字')

    tcp_client_socket.send(download_file.encode('utf-8'))

    recv_data = tcp_client_socket.recv(1024 * 1024)

    with open('./file.txt', "wb") as f:
        f.write(recv_data) 

    tcp_client_socket.close()
    
def __name__ == "__main__":
    main()