import socket

PORT = 9999
IP = '0.0.0.0'
addr = (IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)

server.listen(5)

while True:
    client, addr = server.accept()
    print(client.recv(1024).decode())
    client.send('Hello from Server'.encode()) 