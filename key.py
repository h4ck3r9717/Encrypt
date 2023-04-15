from cryptography.fernet import Fernet

# generate a new encryption key
key = Fernet.generate_key()

# save the key to a file
with open('key.key', 'wb') as file:
    file.write(key)