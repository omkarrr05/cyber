import base64
import random

# 1. Rail Fence Cipher - 2 rails
def rail_fence_encrypt(text):
    result = ""
    for i in range(len(text)):
        if i % 2 == 0:
            result += text[i]
    for i in range(len(text)):
        if i % 2!= 0:
            result += text[i]
    return result

def rail_fence_decrypt(cipher):
    half = (len(cipher) + 1) // 2
    even_chars = cipher[:half]
    odd_chars = cipher[half:]
    result = ""
    for i in range(half):
        result += even_chars[i]
        if i < len(odd_chars):
            result += odd_chars[i]
    return result


# 2. Multiplicative Cipher
def multiplicative_cipher(text, key):
    encrypted = ""
    decrypted = ""

    # Encryption
    for char in text:
        if char.isalpha():
            num = ord(char.upper()) - 65
            enc = (num * key) % 26
            encrypted += chr(enc + 65)
        else:
            encrypted += char

    # Check if key has modular inverse
    try:
        inv_key = pow(key, -1, 26)
    except ValueError:
        return "Invalid key: No modular inverse exists.", ""

    # Decryption
    for char in encrypted:
        if char.isalpha():
            num = ord(char.upper()) - 65
            dec = (num * inv_key) % 26
            decrypted += chr(dec + 65)
        else:
            decrypted += char

    return encrypted, decrypted


# 3. Monoalphabetic Cipher
def mono_encrypt(text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    key = "phqgiumeaylnofdxjkrcvstzwb"
    encrypted = ""
    for char in text.lower():
        if char in plain:
            index = plain.index(char)
            encrypted += key[index]
        else:
            encrypted += char
    return encrypted

def mono_decrypt(cipher_text):
    plain = "abcdefghijklmnopqrstuvwxyz"
    key = "phqgiumeaylnofdxjkrcvstzwb"
    decrypted = ""
    for char in cipher_text.lower():
        if char in key:
            index = key.index(char)
            decrypted += plain[index]
        else:
            decrypted += char
    return decrypted


# 4. Caesar Cipher
def caesar_cipher_encrypt(plain_text, key):
    result = ""
    for i in plain_text:
        if i.isupper():
            result += chr((ord(i) + key - 65) % 26 + 65)
        elif i.islower():
            result += chr((ord(i) + key - 97) % 26 + 97)
        else:
            result += i
    return result

def caesar_cipher_decrypt(cipher_text, key):
    return caesar_cipher_encrypt(cipher_text, -key)


# 5. Vigenere Cipher
def vigenere_encrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
            key_index += 1
        else:
            result += char
    return result

def vigenere_decrypt(text, key):
    result = ""
    key = key.lower()
    key_index = 0
    for char in text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - 97
            if char.isupper():
                result += chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 - shift) % 26 + 97)
            key_index += 1
        else:
            result += char
    return result


# 6. XOR Cipher
def xor_cipher(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) ^ key)
    return result


# 7. Poly-alphabetic - using Vigenere as example
def poly_alphabetic_encrypt(text, key):
    return vigenere_encrypt(text, key)

def poly_alphabetic_decrypt(text, key):
    return vigenere_decrypt(text, key)


# Main Menu
print("1. Caesar Cipher")
print("2. Monoalphabetic")
print("3. Poly-alphabetic / Vigenere")
print("4. Rail fence Cipher")
print("5. Vigenere Cipher")
print("6. XOR Cipher")
print("7. Multiplicative Cipher")

choice = int(input("Enter Your Choice: "))

text = input("Enter text: ")


if choice == 1:
    key = int(input("Enter key: "))
    enc = caesar_cipher_encrypt(text, key)
    dec = caesar_cipher_decrypt(enc, key)
    print("Encryrpted:", enc)

    print("Decrypted:", dec)

elif choice == 2:
    enc = mono_encrypt(text)
    dec = mono_decrypt(enc)
    print("Encrypted:", enc)
    print("Decrypted:", dec)

elif choice == 3 or choice == 5:
    key = input("Enter key word: ")
    enc = poly_alphabetic_encrypt(text, key)
    dec = poly_alphabetic_decrypt(enc, key)
    print("Encrypted:", enc)
    print("Decrypted:", dec)

elif choice == 4:
    enc = rail_fence_encrypt(text)
    dec = rail_fence_decrypt(enc)
    print("Encrypted:", enc)
    print("Decrypted:", dec)

elif choice == 5:
    key = int(input("Enter key 0-255: "))
    enc = xor_cipher(text, key)
    dec = xor_cipher(enc, key)
    print("Encrypted:", base64.b64encode(enc.encode()).decode()) # base64 to display
    print("Decrypted:", dec)

elif choice == 6:
    key = int(input("Enter key: "))
    enc, dec = multiplicative_cipher(text, key)
    print("Encrypted:", enc)
    print("Decrypted:", dec)

else:
    print("Invalid Choice")
