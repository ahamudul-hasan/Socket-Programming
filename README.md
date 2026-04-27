# 🌐 Socket Programming Guide: TCP vs UDP

Welcome to the Socket Programming guide! This repository contains practical examples of **TCP (Transmission Control Protocol)** and **UDP (User Datagram Protocol)** implementations in Python.

---

## 📋 Table of Contents

- [Overview](#overview)
- [TCP Protocol](#tcp-protocol)
- [UDP Protocol](#udp-protocol)
- [TCP vs UDP Comparison](#tcp-vs-udp-comparison)
- [Project Structure](#project-structure)
- [TCP Implementation](#tcp-implementation)
- [UDP Implementation](#udp-implementation)
- [Multi-Threading in Socket Programming](#threading-in-socket-programming)
- [How to Run](#how-to-run)
- [Key Differences Summary](#key-differences-summary)

---

## 🎯 Overview

**Socket programming** is a way to communicate between computers over a network. Two main transport layer protocols are used:

1. **TCP (Transmission Control Protocol)** - Reliable, connection-oriented
2. **UDP (User Datagram Protocol)** - Fast, connectionless

This repository demonstrates both protocols with simple client-server implementations.

---

## 📡 TCP Protocol

### What is TCP?

**TCP (Transmission Control Protocol)** is a **connection-oriented**, **reliable** transport layer protocol that ensures all data is delivered to the destination in the same order it was sent.

### Key Characteristics

| Feature | Description |
|---------|-------------|
| **Connection** | Establishes a connection before data transfer |
| **Reliability** | Guarantees 100% data delivery |
| **Order** | Data arrives in the same order it was sent |
| **Speed** | Slower due to acknowledgments and error checking |
| **Error Checking** | Extensive error detection and correction |
| **Flow Control** | Yes, prevents network congestion |
| **Use Cases** | Email, Web browsing, FTP, SSH, Banking |

### How TCP Works

```
┌─────────┐                                    ┌─────────┐
│ Client  │                                    │ Server  │
└────┬────┘                                    └────┬────┘
     │                                              │
     │────────── SYN (Connection Request) ────────>│
     │                                              │
     │<──────── SYN-ACK (Connection Accept) ────────│
     │                                              │
     │──────── ACK (Acknowledgment) ──────────────>│
     │                                              │
     │      ✓ Connection Established               │
     │                                              │
     │────────── Send Data ───────────────────────>│
     │                                              │
     │<──────── Acknowledgment ───────────────────│
     │                                              │
     │      ✓ Data Transfer Complete               │
     │                                              │
     │────────── FIN (Close) ─────────────────────>│
     │                                              │
```

### TCP Use Cases

✅ **When to use TCP:**
- Email delivery (SMTP)
- Web browsing (HTTP/HTTPS)
- File transfer (FTP)
- Remote login (SSH, Telnet)
- Banking and financial transactions
- Any scenario where **reliability is critical**

---

## 📨 UDP Protocol

### What is UDP?

**UDP (User Datagram Protocol)** is a **connectionless**, **unreliable** transport layer protocol that sends data packets without establishing a connection or guaranteeing delivery.

### Key Characteristics

| Feature | Description |
|---------|-------------|
| **Connection** | No connection establishment required |
| **Reliability** | No guarantee of delivery |
| **Order** | No guarantee of packet order |
| **Speed** | Much faster than TCP |
| **Error Checking** | Minimal error checking |
| **Flow Control** | No flow control |
| **Use Cases** | Video streaming, VoIP, Online games, DNS |

### How UDP Works

```
┌─────────┐                                    ┌─────────┐
│ Client  │                                    │ Server  │
└────┬────┘                                    └────┬────┘
     │                                              │
     │ (No connection setup required)              │
     │                                              │
     │────────── Send Datagram ──────────────────>│
     │                                              │
     │ (No acknowledgment needed)                  │
     │                                              │
     │────────── Send Another Datagram ──────────>│
     │                                              │
     │      ✓ Data sent, no guarantees             │
     │                                              │
```

### UDP Use Cases

✅ **When to use UDP:**
- Live video/audio streaming
- Online multiplayer gaming
- VoIP (Voice over Internet Protocol)
- DNS queries
- IoT sensor data
- Any scenario where **speed is more important than reliability**

---

## 🔄 TCP vs UDP Comparison

### Feature Comparison Table

| Feature | TCP | UDP |
|---------|-----|-----|
| **Connection Setup** | Required (3-way handshake) | Not required |
| **Reliability** | Guaranteed delivery ✓ | Best-effort delivery ✗ |
| **Order Guarantee** | Yes ✓ | No ✗ |
| **Speed** | Slower | Faster ⚡ |
| **Header Size** | 20 bytes (minimum) | 8 bytes (minimum) |
| **Overhead** | High (error checking, flow control) | Low |
| **Broadcasting** | Unicast only | Unicast & Multicast |
| **Error Detection** | Comprehensive | Minimal |
| **Connection Termination** | Graceful close required | Abrupt close OK |
| **Best For** | Accuracy & completeness | Speed & efficiency |

### Visual Comparison

```
TCP: ═══════════════════════════════════════════════════
     Reliable connection, ordered delivery, slower speed

UDP: ───────────────────────────────────────────────────
     Fast packets, no guarantees, minimal overhead
```

---

## 📁 Project Structure

```
Socket Programming/
├── 1_Basic/
│   └── server.py          (Basic Socket Server)
│
├── 2_TCP/
│   ├── server.py          (TCP Server Implementation)
│   └── client.py          (TCP Client Implementation)
│
├── 3_UDP/
│   ├── server.py          (UDP Server Implementation)
│   └── client.py          (UDP Client Implementation)
│
├── 4_Multi_Threading/
│   ├── server.py          (Multi-Threaded TCP Server)
│   └── client.py          (Multi-Threaded TCP Client)
│
├── 5_Practice1/
│   ├── server.py
│   └── client.py
│
├── 6_Practice2/
│   ├── server.py
│   └── client.py
│
└── README.md              (This file)
```

---

## 🔧 TCP Implementation

### TCP Server

```python
import socket

# Create a TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to all interfaces on port 9999
server.bind(('0.0.0.0', 9999))

# Listen for incoming connections (queue up to 5)
server.listen(5)

# Accept connections indefinitely
while True:
    client, addr = server.accept()
    
    # Receive data from client
    print(client.recv(1024).decode())
    
    # Send response back to client
    client.send('Hello from Server'.encode())
```

**Key Points:**
- `socket.SOCK_STREAM` = TCP
- `bind()` - Associates socket with a port
- `listen()` - Waits for incoming connections
- `accept()` - Accepts a client connection
- `recv()` - Receives data
- `send()` - Sends data

### TCP Client

```python
import socket

# Create a TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server at localhost:9999
client.connect(('127.0.0.1', 9999))

# Send data to server
client.send('Hello from Client'.encode())

# Receive response
print(client.recv(1024).decode())
```

**Key Points:**
- `connect()` - Establishes connection with server
- Data is guaranteed to arrive in order
- Connection remains open until explicitly closed

---

## 🚀 UDP Implementation

### UDP Server

```python
import socket

# Create a UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to all interfaces on port 9999
server.bind(('0.0.0.0', 9999))

# Receive data indefinitely
while True:
    data, addr = server.recvfrom(1024)
    
    # Process received data
    print(data.decode())
    
    # Send response back to client address
    server.sendto('Hello from Server'.encode(), addr)
```

**Key Points:**
- `socket.SOCK_DGRAM` = UDP
- No `listen()` or `accept()` needed
- `recvfrom()` - Receives data and sender's address
- `sendto()` - Sends data to specific address
- No connection state

### UDP Client

```python
import socket

# Create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send data to server (connection happens implicitly)
client.sendto('Hello from Client'.encode(), ("127.0.0.1", 9999))

# Receive response
data, addr = client.recvfrom(1024)
print(data.decode())
```

**Key Points:**
- No `connect()` required
- Sends directly with `sendto()`
- `recvfrom()` returns data and sender address
- Fast and simple!

---

## 🧵 Multi-Threading in Socket Programming

### What is Multi-Threading?

**Multi-threading** is a technique that allows a single program to handle **multiple tasks simultaneously**. In socket programming, it enables a server to handle multiple client connections at the same time by creating a new thread for each client.

### Why Multi-Threading?

**Problem:** A basic TCP server can only handle one client at a time. When the server is busy with one client, other clients have to wait.

**Solution:** Multi-threading allows the server to:
- ✅ Handle multiple clients concurrently
- ✅ Keep the main thread available for accepting new connections
- ✅ Prevent one slow client from blocking others
- ✅ Improve server efficiency and responsiveness

### How Multi-Threading Works

```
┌─────────────────────────────────────────────────────────┐
│                    Main Thread                           │
│          (Always listening for new connections)         │
│─────────────────────────────────────────────────────────│
│                                                          │
│  Server accepts Client 1 ──> Creates Thread 1           │
│  Server accepts Client 2 ──> Creates Thread 2           │
│  Server accepts Client 3 ──> Creates Thread 3           │
│                                                          │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐    │
│  │   Thread 1   │ │   Thread 2   │ │   Thread 3   │    │
│  │ Handles      │ │ Handles      │ │ Handles      │    │
│  │ Client 1     │ │ Client 2     │ │ Client 3     │    │
│  │ (Concurrent) │ │ (Concurrent) │ │ (Concurrent) │    │
│  └──────────────┘ └──────────────┘ └──────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

### Multi-Threaded TCP Server Implementation

```python
import socket
import threading

HEADER = 64
PORT = 5050
IP = socket.gethostbyname(socket.gethostname())
ADDR = (IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    """Handle individual client in a separate thread"""
    print(f"[NEW CONNECTION] {addr} connected.")
    
    connected = True
    while connected:
        # Receive message length first
        msg_length = conn.recv(HEADER).decode(FORMAT)
        
        if msg_length:
            msg_length = int(msg_length)
            # Receive the actual message
            msg = conn.recv(msg_length).decode(FORMAT)
            
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[{addr}] {msg}")
    
    conn.close()

def start():
    """Main server loop - accepts connections and creates threads"""
    server.listen()
    print(f"[LISTENING] Server is listening on {ADDR}")
    
    while True:
        # Accept new client connection
        conn, addr = server.accept()
        
        # Create a new thread to handle this client
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        
        # Display number of active threads
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

print("[STARTING] Server is starting....")
start()
```

**Key Points:**
- `threading.Thread()` - Creates a new thread
- `target=handle_client` - Function to run in the thread
- `args=(conn, addr)` - Arguments passed to the target function
- `thread.start()` - Starts the thread execution
- `threading.active_count()` - Returns number of active threads
- Each client runs independently in its own thread

### Multi-Threaded TCP Client

```python
import socket

HEADER = 64
PORT = 5050
IP = "127.0.0.1"  # Change to server IP
ADDR = (IP, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"

def send_message(client, msg):
    """Send a message with header indicating message length"""
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    
    client.send(send_length)
    client.send(message)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

# Send messages
send_message(client, "Hello Server!")
send_message(client, "This is Client 1")
send_message(client, DISCONNECT_MESSAGE)

client.close()
```

### Benefits of Multi-Threading

| Benefit | Description |
|---------|-------------|
| **Concurrency** | Handle multiple clients simultaneously |
| **Responsiveness** | Server doesn't block on one client |
| **Resource Efficient** | Threads are lightweight compared to processes |
| **Scalability** | Can handle many concurrent connections |
| **Simplified Code** | Each thread handles one client independently |

### Common Multi-Threading Patterns

**1. Thread Pool (Limit Thread Count)**
```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(max_workers=10) as executor:
    while True:
        conn, addr = server.accept()
        executor.submit(handle_client, conn, addr)
```

**2. Daemon Threads (Auto-close with Main Program)**
```python
thread = threading.Thread(target=handle_client, args=(conn, addr))
thread.daemon = True  # Thread exits when main program exits
thread.start()
```

**3. Thread Naming for Debugging**
```python
thread = threading.Thread(
    target=handle_client, 
    args=(conn, addr),
    name=f"ClientThread-{addr}"
)
thread.start()
```

### Threading Considerations

⚠️ **Important:**
- **Avoid Race Conditions:** Use locks for shared resources
- **Resource Management:** Limit number of threads to avoid memory issues
- **Thread Safety:** Be careful with shared data between threads
- **Debugging:** Multi-threaded code is harder to debug

### Multi-Threading vs Single-Threading

| Aspect | Single-Threaded | Multi-Threaded |
|--------|-----------------|----------------|
| **Clients Handled** | One at a time | Multiple simultaneously |
| **Blocking** | Yes - others wait | No - each has own thread |
| **Complexity** | Simple | More complex |
| **Resource Usage** | Low | Medium-High |
| **Scalability** | Limited | Better |
| **Real-World Use** | Testing, demos | Production servers |

---

## ▶️ How to Run

### TCP Communication

**Terminal 1 - Start Server:**
```bash
cd TCP
python server.py
```

**Terminal 2 - Run Client:**
```bash
cd TCP
python client.py
```

**Expected Output:**

Server will print:
```
Hello from Client
```

Client will print:
```
Hello from Server
```

---

### UDP Communication

**Terminal 1 - Start Server:**
```bash
cd UDP
python server.py
```

**Terminal 2 - Run Client:**
```bash
cd UDP
python client.py
```

**Expected Output:**

Server will print:
```
Hello from Client
```

Client will print:
```
Hello from Server
```

---

## 🎓 Key Differences Summary

### When Should You Use TCP?

✅ Use TCP when:
- Data accuracy is critical
- You need guaranteed delivery
- Order of data matters
- You can afford the overhead
- Examples: Email, Banking, File Downloads

### When Should You Use UDP?

✅ Use UDP when:
- Speed is more important than reliability
- You can tolerate packet loss
- Order doesn't matter
- You need low latency
- Examples: Video Streaming, Gaming, VoIP

### Quick Decision Guide

```
Need 100% reliable delivery?
    ├─ YES → Use TCP ✓
    └─ NO → Use UDP ⚡

Need ordered data?
    ├─ YES → Use TCP ✓
    └─ NO → Use UDP ⚡

Need low latency?
    ├─ YES → Use UDP ⚡
    └─ NO → Use TCP ✓

Large amounts of data?
    ├─ YES → Use TCP ✓
    └─ NO → Either works
```

---

## 📚 Additional Resources

| Protocol | Learning Resource |
|----------|-------------------|
| **TCP** | [RFC 793](https://tools.ietf.org/html/rfc793) |
| **UDP** | [RFC 768](https://tools.ietf.org/html/rfc768) |
| **Sockets** | [Python Socket Documentation](https://docs.python.org/3/library/socket.html) |

---

## 🎯 Summary Table

| Aspect | TCP | UDP |
|--------|-----|-----|
| **Reliability** | High ✓✓✓ | Low ✗ |
| **Speed** | Moderate ⚡⚡ | High ⚡⚡⚡ |
| **Complexity** | High | Low |
| **Connection** | Stateful | Stateless |
| **Best For** | Web, Email, FTP | Games, Streaming, DNS |

---

## 💡 Tips & Best Practices

### TCP Tips
- Always close connections properly
- Handle connection timeouts
- Use error handling for network failures
- Good for mission-critical data

### UDP Tips
- Implement your own reliability layer if needed
- Handle missing or out-of-order packets
- Use for real-time applications
- Lower overhead = better performance

---

**Happy Socket Programming! 🚀**

*For questions or improvements, feel free to explore and modify the implementations!*
