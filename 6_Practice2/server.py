import socket
import threading

PORT = 5050
FORMAT = 'utf-8'
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected")

    msg = conn.recv(1024).decode(FORMAT)
    print(f"[{addr}] {msg}")

    v_count = count_vowels(msg)

    if v_count == 0:
        response = "Not enough vowels"
    elif v_count <= 2:
        response = "Enough vowels I guess"
    else:
        response = "Too many vowels"

    conn.send(response.encode(FORMAT))
    conn.close()


def start():
    server.listen()
    print("[STARTING] Server is running...")

    while True:
        conn, addr = server.accept()

        # THREAD
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


start()