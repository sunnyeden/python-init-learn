import socket

def main():
    # 创建tcp套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 服务器ip
    server_ip = input('ip')

    # 服务器port
    server_port = input('port')

    # 链接服务器
    tcp_client_socket.connect((server_ip, server_port))

    # 想要发送的数据
    send_data = input('信息')

    # 发送数据
    tcp_client_socket.send(send_data.encode('utf-8'))

    # 接受数据
    recv_data = tcp_client_socket.recv(1024)

    print(recv_data.decode('gbk'))

    # 关闭套接字
    tcp_client_socket.close()
    
if __name__ == "__main__":
    main()