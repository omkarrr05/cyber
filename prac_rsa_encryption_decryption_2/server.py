import socket
# GCD function
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
# Multiplicative inverse
def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None
# Check prime number
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
# Get first prime number
while True:
    p = int(input("Enter a prime number p: "))
    if is_prime(p):
        break
    print("Not a prime number. Try again.")
# Get second prime number
while True:
    q = int(input("Enter a different prime number q: "))
    if is_prime(q) and q != p:
        break
    print("Invalid input. Try again.")
# Key generation
n = p * q
phi = (p - 1) * (q - 1)
# Choose e
e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1
# Calculate d
d = mod_inverse(e, phi)
print("\n=== RSA Key Information ===")
print("Public Key  (e, n):", (e, n))
print("Private Key (d, n):", (d, n))
# Socket setup
server_socket = socket.socket()
server_socket.bind(("localhost", 8080))
server_socket.listen(1)
print("\nWaiting for client connection...")
conn, addr = server_socket.accept()
print("Connected by:", addr)
# Receive encrypted data
data = conn.recv(4096).decode()
cipher_list = list(map(int, data.split(",")))
print("\nEncrypted data received:", cipher_list)
# Decrypt each value
raw_values = [pow(c, d, n) for c in cipher_list]
print("Raw decrypted values:", raw_values)
# Convert ASCII values to characters
decrypted = ""
for m in raw_values:
    if 32 <= m <= 126:
        decrypted += chr(m)
    else:
        decrypted += "?"
print("Decrypted message:", decrypted)
# Close connection
conn.close()
server_socket.close()
