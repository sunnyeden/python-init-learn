```python
from socket import *

def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCKET_DGRAM)

    udp_socket.bind('', 7788)

    while True:
        udp_ip = input('请输入ip')
        udp_port = int(input('请输入port'))
        upd_msg = input('请输入发送数据')
        udp_socket.sendto(upd_msg.encode('utf-8'), (udp_ip, udp_port))

        recv_data, recv_addr  = udp_socket.recvfrom(1024)

        print("%s:%s" % (recv_addr, recv_data))

def __name__ == "__main__":
    print('-' * 50)
    print('python 聊天室')
    print('-' * 50)
    main()
```