import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('0.0.0.0', 9999))

while True:
    data, addr = server.recvfrom(1024)
    print(data.decode())
    server.sendto('Hello from Server'.encode(), addr)