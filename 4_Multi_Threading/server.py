import socket

PORT = 5050
IP = socket.gethostbyname(socket.gethostname())
addr = (IP, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(addr)