# import the necessary modules
import argparse
from cryptography.fernet import Fernet
from PIL import Image

# initialize the argument parser
parser = argparse.ArgumentParser(description='Encrypt and decrypt files using a password.')

# add the command line arguments
parser.add_argument('--encrypt', action='store_true', help='Encrypt a file')
parser.add_argument('--decrypt', action='store_true', help='Decrypt a file')
parser.add_argument('--password', required=True, help='Password to encrypt or decrypt file')
parser.add_argument('--input', required=True, help='Input file path')
parser.add_argument('--output', required=True, help='Output file path')
parser.add_argument('--file', required=True, help='File to encrypt')

# parse the arguments
args = parser.parse_args()

# load the encryption key from the file
with open('key.key', 'rb') as file:
    key = file.read()

# initialize the Fernet object with the encryption key
fernet = Fernet(key)

# read the input file
with open(args.file, 'rb') as file:
    file_data = file.read()

# encrypt the file data
encrypted_file_data = fernet.encrypt(file_data)

# read the input image
input_image = Image.open(args.input)

# convert the image to RGB mode
rgb_input_image = input_image.convert('RGB')

# get the size of the image
width, height = rgb_input_image.size

# create a new image to store the encrypted file data
encrypted_image = Image.new('RGB', (width, height), color=0)

# get the pixels of the input image
pixels = rgb_input_image.load()

# iterate over each pixel of the image and embed the encrypted file data
index = 0
for i in range(width):
    for j in range(height):
        # get the pixel at the current position
        pixel = pixels[i, j]

        # check if all bytes of the encrypted file data have been embedded
        if index < len(encrypted_file_data):
            # get the next byte of the encrypted file data
            byte = encrypted_file_data[index]
            index += 1

            # embed the byte into the least significant bit of each color channel of the pixel
            r, g, b = pixel
            r &= 0xFE
            r |= (byte & 0x01)
            g &= 0xFE
            g |= ((byte >> 1) & 0x01)
            b &= 0xFE
            b |= ((byte >> 2) & 0x01)
            pixels[i, j] = (r, g, b)

# save the encrypted image
rgb_input_image.save(args.output)
print(f"Encrypted file '{args.file}' stored in image '{args.output}'.")
#n