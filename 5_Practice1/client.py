import socket

HEADER = 1024
PORT = 5050
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

message = input("Enter message: ")

client.send(message.encode(FORMAT))

response = client.recv(HEADER).decode(FORMAT)
print("Server:", response)

client.close()