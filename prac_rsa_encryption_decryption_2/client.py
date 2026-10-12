import socket

# Encryption function
def encrypt(message, e, n):
    cipher = [pow(ord(char), e, n) for char in message]

    print("Plaintext ASCII values:",
          [ord(char) for char in message])

    print("Encrypted values:", cipher)

    return cipher
# Enter server public key
e = int(input("Enter server public key e: "))
n = int(input("Enter server public key n: "))


# Enter message
message = input("Enter message to send: ")


# Encrypt message
cipher = encrypt(message, e, n)


# Create socket
client_socket = socket.socket()

# Connect to server
client_socket.connect(("localhost", 9999))


# Convert list to comma-separated string
data = ",".join(map(str, cipher))


# Send encrypted data
client_socket.send(data.encode())

print("\nEncrypted message sent:", cipher)


# Close socket
client_socket.close()
