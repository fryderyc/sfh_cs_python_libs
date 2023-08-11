from cryptography.fernet import Fernet

# Generate a new encryption key
def generate_key():
    key = Fernet.generate_key()
    with open("encryption.key", "wb") as file:
        file.write(key)

# Read the encryption key from file
def load_key():
    with open("encryption.key", "rb") as file:
        key = file.read()
    return key

# Encrypt a message
def encrypt_message(message, key):
    cipher = Fernet(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

# Decrypt a message
def decrypt_message(encrypted_message, key):
    cipher = Fernet(key)
    decrypted_message = cipher.decrypt(encrypted_message)
    return decrypted_message.decode()

def main():
    generate_key() # Run this line only once to generate the encryption key
    
    key = load_key()

    message = input("Enter a message to encrypt: ")
    encrypted = encrypt_message(message, key)

    print("Encrypted message:", encrypted.decode())

    decrypted = decrypt_message(encrypted, key)
    print("Decrypted message:", decrypted)

if __name__ == '__main__':
    main()