from crypto_utils import generate_key, encrypt_message, decrypt_message
from stegano_utils import encode_image, decode_image

def main():
    print("🔐 Secure Image Steganography Tool (Fast Version)")
    print("1. Hide a secret message")
    print("2. Extract hidden message")
    choice = input("Select option (1/2): ")

    if choice == '1':
        message = input("Enter secret message: ")
        key = generate_key()
        encrypted = encrypt_message(key, message)

        image_name = input("Enter source image filename (e.g. secret_image.png): ")
        output_image = input("Enter output filename (e.g. stego_image.png): ")

        try:
            encode_image(image_name, encrypted, output_image)
            print(f"✅ Message embedded successfully in '{output_image}'")
            print(f"🔑 Save this key securely:\n{key.decode()}")
        except Exception as e:
            print(f"❌ Error: {e}")

    elif choice == '2':
        key_input = input("Enter your secret key: ").encode()
        stego_image = input("Enter image filename (e.g. stego_image.png): ")

        try:
            encrypted = decode_image(stego_image)
            decrypted = decrypt_message(key_input, encrypted)
            print(f"🔓 Hidden message: {decrypted}")
        except Exception as e:
            print(f"❌ Failed to decrypt message: {e}")

if __name__ == "__main__":
    main()
# This script provides a simple command-line interface for hiding and extracting messages in images using steganography.