import os

from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64

SALT_SIZE = 32


def derive_key_from_password(password, salt):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=480000,
        salt=salt,
        backend=default_backend(),
        length=SALT_SIZE
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    return key


def encrypt_message_with_password(message, password, output_file):
    salt = os.urandom(SALT_SIZE)
    key = derive_key_from_password(password.encode(), salt)
    fernet_key = Fernet(key)
    ciphertext = fernet_key.encrypt(message.encode())

    with open(output_file, 'wb') as f:
        f.write(salt)
        f.write(ciphertext)


def decrypt_message_with_password(input_file, password):
    with open(input_file, 'rb') as f:
        salt = f.read(SALT_SIZE)
        ciphertext = f.read()

    key = derive_key_from_password(password.encode(), salt)
    fernet_key = Fernet(key)
    try:
        decrypted_message = fernet_key.decrypt(ciphertext).decode()
        return decrypted_message
    except Exception as e:
        print("Decryption failed. Check your password.")
        return None
