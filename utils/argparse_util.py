import argparse


def create_parser():
    parser = argparse.ArgumentParser(description="Encrypt and decrypt a message with a password")
    parser.add_argument("module", choices=["nacl", "fernet"], help="Choose a cryptographic module (e.g., 'nacl', "
                                                                   "'fernet')")
    parser.add_argument("action", choices=["enc", "dec"], help="Choose 'enc -> encrypt' or 'dec -> decrypt' action")
    parser.add_argument("-f", "--file", help="Input file for decryption, output file for encryption")
    parser.add_argument("-p", "--password", help="Password for encryption or decryption")
    parser.add_argument("-m", "--message", help="Message to encrypt")
    return parser


def print_usage():
    print("Usage: python lcft.py <module> <action> -f input_file -p password")
    print("Modules:")
    print("  nacl      - Use PyNaCl for encryption and decryption.")
    print("  fernet    - Use fernet for encryption and decryption.")
    print("Actions:")
    print("  enc       - Encrypt a message.")
    print("  dec       - Decrypt a message.")
    print("Examples:")
    print("  python lcft.py nacl enc -f secret.txt -p password123 -m 'My secret message'")
    print("  python lcft.py nacl dec -f secret.txt -p password123")
