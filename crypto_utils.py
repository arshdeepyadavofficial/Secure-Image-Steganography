from cryptography.fernet import Fernet

def generate_key() -> bytes:
    return Fernet.generate_key()

def encrypt_message(key: bytes, message: str) -> bytes:
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(key: bytes, encrypted: bytes) -> str:
    f = Fernet(key)
    return f.decrypt(encrypted).decode()
