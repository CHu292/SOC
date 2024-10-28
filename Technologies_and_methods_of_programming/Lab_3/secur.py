import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.exceptions import InvalidSignature
from cryptography.fernet import Fernet
import subprocess

PUBLIC_KEY_FILE = "public_key.pem"
SIGNATURE_FILE = "signature.dat"
SYS_FILE = "sys.tat"

def get_signature_from_file():
    try:
        with open(SIGNATURE_FILE, "rb") as f:
            return f.read()
    except FileNotFoundError:
        print(f"File chữ ký không tồn tại: {SIGNATURE_FILE}")
        return None

def load_public_key_from_file(public_key_file):
    try:
        with open(public_key_file, "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        return public_key
    except FileNotFoundError:
        print(f"File khóa công khai không tồn tại: {public_key_file}")
        return None

def verify_signature(public_key, message, signature):
    try:
        public_key.verify(
            signature,
            message,
            padding.PKCS1v15(),
            hashes.SHA256()
        )
        return True
    except InvalidSignature:
        return False
    
def decrypt_file(filepath, key):
    cipher_suite = Fernet(key)
    with open(filepath, 'rb') as file:
        encrypted_data = file.read()
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    
    with open(filepath, 'wb') as file:
        file.write(decrypted_data)

def encrypt_file(filepath, key):
    cipher_suite = Fernet(key)
    with open(filepath, 'rb') as file:
        file_data = file.read()
    encrypted_data = cipher_suite.encrypt(file_data)
    
    with open(filepath, 'wb') as file:
        file.write(encrypted_data)


def main():
    signature = get_signature_from_file()
    if not signature:
        return

    public_key = load_public_key_from_file(PUBLIC_KEY_FILE)
    if not public_key:
        return

    message = b"sysinfo"
    
    if verify_signature(public_key, message, signature):
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
        decrypt_file(SYS_FILE, key)
        subprocess.run(['nano', SYS_FILE])
        encrypt_file(SYS_FILE, key)
    else:
        print("Xác thực không thành công! Không thể mở file sys.tat.")

if __name__ == "__main__":
    main()

