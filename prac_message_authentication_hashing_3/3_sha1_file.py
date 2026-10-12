import hashlib

# Open the file in read mode
with open("message.txt", "r") as file:
    message = file.read()

# Convert the message into bytes
message_bytes = message.encode()

# Generate SHA1 hash
message_hash = hashlib.sha1(message_bytes)

# Convert hash into readable hexadecimal format
hash_value = message_hash.hexdigest()

# Display the original message and hash value
print("\n--- File Content ---")
print("Original Message:", message)

print("\n--- SHA1 Hash ---")
print("Hash Value:", hash_value)
