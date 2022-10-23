from hashlib import sha256
print("Please enter password to be hashed:")
passwd = input()
hashed = sha256(passwd.encode()).hexdigest()
print("Hashed password:\n" + hashed)
