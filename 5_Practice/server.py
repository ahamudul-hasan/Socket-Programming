import socket

HEADER = 1024
PORT = 5050
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)
FORMAT = 'utf-8'

def count_vowel(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr}")

    msg = conn.recv(HEADER).decode(FORMAT)
    print(f"[{addr}] {msg}")

    v_count = count_vowel(msg)

    if v_count == 0:
        response = "Not enough vowels"
    elif v_count <= 2:
        response = "Enough vowels I guess"
    else:
        response = "Too many vowels"
    
    conn.send(response.encode(FORMAT))
    conn.close()

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)

    server.listen()
    print(f"[STARTING] server is running....")

    while True:
        conn, addr = server.accept()
        handle_client(conn, addr)

start()