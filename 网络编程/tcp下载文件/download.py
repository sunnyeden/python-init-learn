import socket

def main():
    # 创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = input('ip')
    server_port = input('port')

    # 链接服务器
    tcp_client_socket.connect((server_ip, server_port))

    download_file = input('请输入要下载的文件名字')

    tcp_client_socket.send(download_file.encode('utf-8'))

    recv_data = tcp_client_socket.recv(1024 * 1024)

    # 保存数据到文件
    with open('./file.txt', "wb") as f:
        f.write(recv_data) 

    # 关闭套接字
    tcp_client_socket.close()
    
if __name__ == "__main__":
    main()