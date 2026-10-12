import math
def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a
# Prime numbers
p = int(input("Enter 1st prime no.: "))
q = int(input("Enter 2nd prime no.: "))
# Compute n and phi
n = p * q
phi = (p - 1) * (q - 1)
# Choose e such that e and phi(n) are coprime
e = 3
while e < phi:
    if gcd(e, phi) == 1:
        break
    else:
        e += 2
# Compute d (multiplicative inverse of e mod phi)
def multiplicative_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None
d = multiplicative_inverse(e, phi)
# Check if inverse exists
if d is None:
    print("Error: Could not find multiplicative inverse of e")
    exit()
# Message to encrypt
pt = int(input("Enter msg in number: "))
print("Plain text:", pt)
# Encryption
c = pow(pt, e, n)
print("Encrypted msg:", c)
# Decryption
decrypt = pow(c, d, n)
print("Decrypted msg:", decrypt)
