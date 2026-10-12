# Practical 07 - Web Security with SSL/TLS (certificate creation)
# Run these in Git Bash (Git for Windows). Passphrase used in the practical: 12345678

# 1. Generate a 2048-bit RSA private key protected with 3DES
winpty openssl genrsa -des3 -out Namrata.key 2048

# 2. Create a self-signed root certificate valid for 1825 days (5 years)
openssl req -x509 -new -nodes -key Namrata.key -sha256 -days 1825 -out Namrata.pem

# 3. Import into Windows (GUI steps):
#    Win+R -> mmc -> File -> Add/Remove Snap-in -> Certificates -> Computer account -> Local computer
#    Trusted Root Certification Authorities -> right-click -> All Tasks -> Import -> select Namrata.pem
