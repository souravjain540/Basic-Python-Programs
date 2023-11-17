# pip install cryptography

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
import os

def pad(data):
    block_size = algorithms.AES.block_size // 8
    padding = block_size - len(data) % block_size
    return data + bytes([padding] * padding)

def unpad(data):
    padding = data[-1]
    return data[:-padding]

def encrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        plaintext = file.read()

    plaintext = pad(plaintext)

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(output_file, 'wb') as file:
        file.write(ciphertext)

def decrypt_file(input_file, output_file, key):
    with open(input_file, 'rb') as file:
        ciphertext = file.read()

    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    plaintext = unpad(plaintext)

    with open(output_file, 'wb') as file:
        file.write(plaintext)

if __name__ == "__main__":
    # Example usage
    input_file = "example.txt"
    encrypted_file = "example_encrypted.txt"
    decrypted_file = "example_decrypted.txt"

    # Generate a random 256-bit key (32 bytes)
    key = os.urandom(32)

    # Encrypt the file
    encrypt_file(input_file, encrypted_file, key)

    print(f"File '{input_file}' encrypted to '{encrypted_file}'")

    # Decrypt the file
    decrypt_file(encrypted_file, decrypted_file, key)

    print(f"File '{encrypted_file}' decrypted to '{decrypted_file}'")
