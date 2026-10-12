import hashlib

# Get messages from the user
message1 = input("Enter the first message: ")
message2 = input("Enter the second message: ")

# Convert messages from string to bytes
message1_bytes = message1.encode()
message2_bytes = message2.encode()

# Generate SHA1 hash for each message
message1_hash = hashlib.sha1(message1_bytes)
message2_hash = hashlib.sha1(message2_bytes)

# Convert hash values into readable hexadecimal format
message1_hash_value = message1_hash.hexdigest()
message2_hash_value = message2_hash.hexdigest()

# Display the original messages and their hash values
print("\n--- Message 1 ---")
print("Original Message:", message1)
print("SHA1 Hash:", message1_hash_value)

print("\n--- Message 2 ---")
print("Original Message:", message2)
print("SHA1 Hash:", message2_hash_value)
