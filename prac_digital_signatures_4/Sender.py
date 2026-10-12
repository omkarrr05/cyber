from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
# Input message from sender
message = input("Sender: Enter your message: ")
# Save the message
with open("message.txt", "w") as f:
    f.write(message)
# Generate RSA key pair
random_generator = Random.new().read
key_pair = RSA.generate(2048, random_generator)
# Extract private and public keys
private_key = key_pair.export_key()
public_key = key_pair.publickey().export_key()
# Display public key
print("\nSender: Public Key:\n")
print(public_key.decode())
# Function to generate digital signature
def generate_signature(private_key, message):
    # Import private key
    key = RSA.import_key(private_key)
    # Create SHA-256 hash
    hashed_message = SHA256.new(message.encode("utf-8"))
    # Create signer using private key
    signer = PKCS1_v1_5.new(key)
    # Generate digital signature
    signature = signer.sign(hashed_message)

    return signature


# Generate digital signature
signature = generate_signature(private_key, message)

# Save public key
with open("public_key.txt", "wb") as f:
    f.write(public_key)

# Save digital signature
with open("signature.sig", "wb") as f:
    f.write(signature)

print("\nSender: All data saved.")
print("Sender: Message sent:", message)
print("Sender: Digital signature generated and saved.")
