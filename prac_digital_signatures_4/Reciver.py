
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA


# Function to verify digital signature
def verify_signature(public_key_data, message, signature):

    # Import public key
    key = RSA.import_key(public_key_data)

    # Create SHA-256 hash of received message
    hashed_message = SHA256.new(message.encode("utf-8"))

    # Create verifier using public key
    verifier = PKCS1_v1_5.new(key)

    # Verify signature
    return verifier.verify(hashed_message, signature)


# Load public key
with open("public_key.txt", "rb") as f:
    public_key = f.read()


# Load digital signature
with open("signature.sig", "rb") as f:
    signature = f.read()


# Input the original message
message = input("Receiver: Enter the original message: ")


# Verify the signature
if verify_signature(public_key, message, signature):
    print("\nReceiver: Signature is VALID.")
    print("Message is authentic.")
else:
    print("\nReceiver: Signature is INVALID.")
    print("Message may have been altered.")
