import socket

PORT = 5050
FORMAT = 'utf-8'
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

message = input("Enter message: ")

client.send(message.encode(FORMAT))

response = client.recv(1024).decode(FORMAT)
print("Server:", response)

client.close()