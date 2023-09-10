import nacl.utils

from nacl.secret import SecretBox
from nacl.pwhash import argon2i

KEY_SIZE = SecretBox.KEY_SIZE
NONCE_SIZE = SecretBox.NONCE_SIZE
SALT_SIZE = argon2i.SALTBYTES


def generate_key_from_password(password, salt):
    key = argon2i.kdf(KEY_SIZE, password.encode(), salt, opslimit=argon2i.OPSLIMIT_INTERACTIVE,
                      memlimit=argon2i.MEMLIMIT_INTERACTIVE)
    return key


def encrypt_message_with_password(message, password, output_file):
    salt = nacl.utils.random(SALT_SIZE)
    key = generate_key_from_password(password, salt)
    box = SecretBox(key)
    nonce = nacl.utils.random(NONCE_SIZE)
    ciphertext = box.encrypt(message.encode(), nonce)

    assert len(ciphertext) == len(message) + box.NONCE_SIZE + box.MACBYTES

    with open(output_file, 'wb') as f:
        f.write(salt)
        f.write(ciphertext)

    decrypted_message = box.decrypt(ciphertext).decode()
    print(f"Decrypted message: {decrypted_message}")


def decrypt_message_with_password(input_file, password):
    with open(input_file, 'rb') as f:
        salt = f.read(SALT_SIZE)
        ciphertext = f.read()

    key = generate_key_from_password(password, salt)
    box = SecretBox(key)

    try:
        decrypted_message = box.decrypt(ciphertext).decode()
        return decrypted_message
    except ValueError as e:
        print("Decryption failed. Check your password.")
        return None
