import socket

name = socket.gethostname()
ip = socket.gethostbyname(socket.gethostname())

print(name)
print(ip)