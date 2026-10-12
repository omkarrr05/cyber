# Diffie-Hellman Client Program

import socket

# Client private key
b = int(input("Enter private key of client (b): "))

# Connect to server
client = socket.socket()
client.connect(('localhost', 8080))

# Receive public parameters and server public key
data = client.recv(1024).decode()
p, g, A = map(int, data.split(','))

# Compute client's public key
B = pow(g, b, p)

print("\nClient Info")
print(f"Received public parameters: p = {p}, g = {g}")
print(f"Received Server public key (A): {A}")
print(f"Client private key (b): {b}")
print(f"Client public key (B = g^b mod p): {B}")

# Send client's public key to server
client.send(str(B).encode())

# Compute shared secret
shared_secret = pow(A, b, p)

print(f"Shared secret (A^b mod p): {shared_secret}")

client.close()
