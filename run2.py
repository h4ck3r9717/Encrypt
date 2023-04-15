# import the necessary modules
import argparse
from cryptography.fernet import Fernet

# initialize the argument parser
parser = argparse.ArgumentParser(description='Encrypt and decrypt files using a password.')

# add the command line arguments
parser.add_argument('--encrypt', action='store_true', help='Encrypt a file')
parser.add_argument('--decrypt', action='store_true', help='Decrypt a file')
parser.add_argument('--password', required=True, help='Password to encrypt or decrypt file')
parser.add_argument('--input', required=True, help='Input file path')
parser.add_argument('--output', required=True, help='Output file path')

# parse the arguments
args = parser.parse_args()

# load the encryption key from the file
with open('key.key', 'rb') as file:
    key = file.read()

# initialize the Fernet object with the encryption key
fernet = Fernet(key)

# read the input file
with open(args.input, 'rb') as file:
    input_data = file.read()

# encrypt or decrypt the input data based on the user's choice
if args.encrypt:
    output_data = fernet.encrypt(input_data)
    with open(args.output, 'wb') as file:
        file.write(output_data)
        print(f"Encrypted message saved to file '{args.output}'.")
elif args.decrypt:
    try:
        output_data = fernet.decrypt(input_data)
        with open(args.output, 'wb') as file:
            file.write(output_data)
            print(f"Decrypted message saved to file '{args.output}'.")
    except:
        print("Error: Could not decrypt the input file with the provided password.")