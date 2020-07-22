import socket

def main():
    # 创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.bind(('', 7890))
    tcp_server_socket.listen(128)

    while True:
        # 循环等待用户链接
        print("正则等待新用户链接...")
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("客服正在为 %s:%s 服务" % (client_addr[0], client_addr[1]))

        while True:
            # 循环为用户提供服务
            recv_data = new_client_socket.recv(1024)
            print(recv_data.decode('gbk'))
            if recv_data:
                new_client_socket.send('hello'.encode('gbk'))
            else:
                break

if __name__ == "__main__":
    main()

