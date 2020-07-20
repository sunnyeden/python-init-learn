#encoding=utf-8

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9999))

print("udp server is running")

while True:
    data, addr = s.recvfrom(1024)
    print(data.decode('utf-8'), addr)
    s.sendto(b'hello', addr)