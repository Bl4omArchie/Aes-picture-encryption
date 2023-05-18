from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from PIL import Image
import os


# Define the encryption function
def encrypt_pixels(pixel_list, key):
    cipher = AES.new(key, AES.MODE_CBC)
    pixel_bytes = bytes(pixel_list)
    padded_bytes = pad(pixel_bytes, AES.block_size)
    encrypted_bytes = cipher.encrypt(padded_bytes)

    return cipher.iv, encrypted_bytes

# Define the decryption function
def decrypt_pixels(encrypted_bytes, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_bytes = cipher.decrypt(encrypted_bytes)
    unpadded_bytes = unpad(decrypted_bytes, AES.block_size)
    pixel_list = list(unpadded_bytes)

    return pixel_list


# Example usage
key = os.urandom(16)
image_path = 'linux.jpeg'

with Image.open(image_path) as img:
    pixel_list = list(img.getdata())
iv, encrypted_bytes = encrypt_pixels(pixel_list, key)


encrypted_pixel_list = list(encrypted_bytes)
encrypted_img = Image.new(img.mode, img.size)
encrypted_img.putdata(encrypted_pixel_list)
encrypted_img.save('linux.jpeg')


with Image.open('my_encrypted_image.jpg') as img:
    encrypted_pixel_list = list(img.getdata())

encrypted_bytes = bytes(encrypted_pixel_list)
pixel_list = decrypt_pixels(encrypted_bytes, key, iv)
decrypted_img = Image.new(img.mode, img.size)
decrypted_img.putdata(pixel_list)
decrypted_img.save('linux.jpeg')