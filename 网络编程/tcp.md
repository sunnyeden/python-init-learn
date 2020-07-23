#### tcp客户端

```python
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
```

#### tcp服务端

```Python
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
```

#### tcp下载文件

```python
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
```
