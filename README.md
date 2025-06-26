# 🔐 Secure Image Steganography Tool

This is a simple Python-based project that allows you to securely hide and extract text messages inside images using steganography and AES encryption.

## 📌 About the Project

Steganography is the art of hiding information inside other files. In this project, a secret message is first encrypted using the AES algorithm (via Python's cryptography library) and then hidden inside a PNG image using Least Significant Bit (LSB) steganography.

The final image looks visually unchanged but holds the hidden message securely.

## 🛠 Features

- AES-based encryption (Fernet)
- Fast and secure text embedding into PNG images
- Length-based decoding (no EOF marker)
- Works with small or large images
- CLI-based interface using Python

## 🧑‍💻 How It Works

1. User inputs a message.
2. The message is encrypted using AES.
3. Encrypted data is embedded into the image’s RGB pixels using LSB.
4. Image is saved with the hidden message.
5. During decoding, bits are extracted and decrypted using the provided key.

## 📁 File Structure

- main.py → CLI tool to run the encoder/decoder
- crypto_utils.py → Handles encryption and decryption
- stegano_utils.py → Functions to encode and decode image bits
- arsh.png → Output image with hidden message
- ves.png → Sample source image

## ▶️ How to Run

1. Make sure Python is installed (version 3.8+ recommended)
2. Install dependencies:

   ```
   pip install cryptography pillow
   ```

3. Run the main script:

   ```
   python main.py
   ```

4. Follow the prompts to encode or decode a message.

## 💬 Example

Encoding:

```
Enter secret message: Hello Arshdeep
Enter source image filename: ves.png
Enter output filename: arsh.png
```

Decoding:

```
Enter your secret key: <your-key>
Enter image filename: arsh.png
→ Hidden message: Hello Arshdeep
```

## 🔒 Security Note

The encrypted message is unreadable without the correct Fernet key. The stego image itself gives no clue that it holds hidden data.

```
## 🏁 Future Improvements

- GUI interface with file upload
- Support for other formats (audio, video)
- File compression before encryption

```
## 👤 Author

Made with 🖤 by Arshdeep Yadav  
Computer Science Engineering,<br>
R.E.C. Kannauj

```
## 📄 License

This project is licensed under the [MIT License](LICENSE).  
Feel free to use, modify, and share it with proper attribution.

```
