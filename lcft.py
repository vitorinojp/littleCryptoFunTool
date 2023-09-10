import os
import sys
from utils.argparse_util import create_parser, print_usage
from utils.password_utils import generate_password
from modules.nacl.nacl_util import encrypt_message_with_password, decrypt_message_with_password
from modules.fernet.fernet_util import encrypt_message_with_password, decrypt_message_with_password


def main():
    if len(sys.argv) < 2:
        print_usage()
        sys.exit(1)

    parser = create_parser()
    args = parser.parse_args()

    module = args.module
    action = args.action
    file = args.file
    password = args.password
    message = args.message

    if not file:
        file = "output/secret." + module
    try:
        f = open(file)
        f.close()
    except FileNotFoundError:
        open(file, 'a').close()

    # if the password is not set, randomly generate one
    if not password:
        password = generate_password()
        print(f"Generated password: {password}")

    if module == "nacl":
        if action == "enc":
            encrypt_message_with_password(message, password, file)
            print(f"Message encrypted and saved to {file}")
        elif action == "dec":
            decrypted_message = decrypt_message_with_password(file, password)
            if decrypted_message:
                print(f"Decrypted message: {decrypted_message}")
    elif module == "fernet":
        if action == "enc":
            encrypt_message_with_password(message, password, file)
            print(f"Message encrypted and saved to {file}")
        elif action == "dec":
            decrypted_message = decrypt_message_with_password(file, password)
            if decrypted_message:
                print(f"Decrypted message: {decrypted_message}")
    else:
        print(f"Invalid module: {module}. Supported modules: nacl, fernet")


if __name__ == "__main__":
    main()
