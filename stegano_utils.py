from PIL import Image

def _int_to_bin(data: bytes) -> str:
    return ''.join(f'{byte:08b}' for byte in data)

def _bin_to_bytes(binary_data: str) -> bytes:
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    return bytes([int(b, 2) for b in all_bytes])

def encode_image(image_path: str, data: bytes, output_path: str):
    img = Image.open(image_path).convert("RGB")  # ⬅️ ensures pixel is (R, G, B)
    pixels = list(img.getdata())

    # Encode message length as 32-bit integer (in bits)
    length = len(data)
    length_bin = f"{length:032b}"
    data_bin = length_bin + _int_to_bin(data)
    data_index = 0

    new_pixels = []

    for pixel in pixels:
        r, g, b = pixel
        new_colors = []

        for color in (r, g, b):
            if data_index < len(data_bin):
                new_color = (color & ~1) | int(data_bin[data_index])
                data_index += 1
            else:
                new_color = color
            new_colors.append(new_color)

        new_pixels.append(tuple(new_colors))

        if data_index >= len(data_bin):
            break

    if data_index < len(data_bin):
        raise ValueError("Image is too small to hold the message.")

    img.putdata(new_pixels + pixels[len(new_pixels):])
    img.save(output_path)

def decode_image(image_path: str) -> bytes:
    img = Image.open(image_path).convert("RGB")  # ⬅️ ensures pixel is (R, G, B)
    pixels = list(img.getdata())

    binary_data = ''
    for pixel in pixels:
        for color in pixel[:3]:  # Only RGB
            binary_data += str(color & 1)

    # First 32 bits = message length (in bytes)
    length = int(binary_data[:32], 2)
    message_bits = binary_data[32:32 + (length * 8)]

    if len(message_bits) < length * 8:
        raise ValueError("Image does not contain enough data.")

    return _bin_to_bytes(message_bits)
def decode_image_safe(image_path: str) -> bytes:
    try:
        return decode_image(image_path)
    except Exception as e:
        print(f"Error decoding image: {e}")
        return b''
    