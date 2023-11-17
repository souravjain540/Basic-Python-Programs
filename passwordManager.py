# pip install cryptography

from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self, key):
        self.key = key
        self.cipher = Fernet(key)
        self.passwords = {}

    def encrypt(self, data):
        return self.cipher.encrypt(data.encode())

    def decrypt(self, data):
        return self.cipher.decrypt(data).decode()

    def add_password(self, service, username, password):
        encrypted_password = self.encrypt(password)
        self.passwords[service] = {'username': username, 'password': encrypted_password}

    def get_password(self, service):
        if service in self.passwords:
            encrypted_password = self.passwords[service]['password']
            decrypted_password = self.decrypt(encrypted_password)
            return decrypted_password
        else:
            return None

    def update_password(self, service, new_password):
        if service in self.passwords:
            encrypted_password = self.encrypt(new_password)
            self.passwords[service]['password'] = encrypted_password
            return True
        else:
            return False

if __name__ == "__main__":
    # Example usage
    key = Fernet.generate_key()
    password_manager = PasswordManager(key)

    # Add a password
    password_manager.add_password('example', 'user123', 'securePassword123')

    # Retrieve a password
    retrieved_password = password_manager.get_password('example')
    print(f"Retrieved Password: {retrieved_password}")

    # Update a password
    password_manager.update_password('example', 'newSecurePassword456')

    # Retrieve the updated password
    updated_password = password_manager.get_password('example')
    print(f"Updated Password: {updated_password}")
