import socket

# Public parameters
p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

# Server private and public key
a = int(input("Enter private key for server (a): "))
A = pow(g, a, p)

print("\nServer info")
print(f"Public parameters: p = {p}, g = {g}")
print(f"Server private key (a): {a}")
print(f"Server public key (A = g^a mod p): {A}")

# Set up server socket
server = socket.socket()
server.bind(('localhost', 8080))
server.listen(1)

print("\nServer listening for connection...")

conn, addr = server.accept()
print(f"Connected by {addr}")

# Send public parameters and server's public key
conn.send(f"{p},{g},{A}".encode())

# Receive client's public key
data = conn.recv(1024).decode()
B = int(data)

# Compute shared secret
shared_secret = pow(B, a, p)

print(f"\nReceived client public key (B): {B}")
print(f"Shared secret (client) (B^a mod p): {shared_secret}")

conn.close()
