from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from PIL import Image
import numpy as np
import os


def generate_key():
    key = os.urandom(16)
    iv = os.urandom(16)

    with open("key.txt", "a") as fp:
        fp.write(f"key: {key} \niv: {iv}")
        fp.write("\n==============================================\n\n")
    return key, iv


def load_picture(filename):
    # Load the image and convert it to a NumPy array
    img = Image.open(filename)
    img_arr = np.array(img)
    return img_arr


def encrypt_picture(key, iv, img_arr, filename):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    img_arr_padded = pad(img_arr.flatten().tobytes(), AES.block_size)
    encrypted_data = cipher.encrypt(img_arr_padded)

    with open(filename, "wb") as f:
        f.write(encrypted_data)

def decrypt_picture():
    pass


if __name__ == "__main__":
    filename = "haxordog.jpg"

    key, iv = generate_key()
    img = load_picture(filename)
    encrypt_picture(key, iv, img, filename)