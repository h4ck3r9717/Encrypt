## Encryption
Developed by **h4ck3r** 

It allows you to encrypt your documens and files using a your password of your choice.


### Target Audience
This project targets people such as:
- Scammers
- Hackers
- Spies
- Annybody


## Technologies Used

- Python3.10
- linux *(arch linux)*

# Prerequisites

To work with tool you need to have some few prerequisites.

- Python3.10

- pip *(You will need to install the requirements = pip install -r requirements.txt)*

- virtualenv

- Code/text editor **Visul studio code** which is the best

- Terminal

# How it works
**Encrypting**

- python3.10 run2.py --encrypt --password <password> --input <input_file> --output <output_file>
   **e.g*
- python3.10 run2.py --encrypt --password 123 --input njoga.txt --output encrypted.txt

**Decryption**

- python3.10 run2.py --decrypt --password nasa9717 --input  --output <output_file>
    **e.g*
- python3.10 run2.py --decrypt --password nasa9717 --input encrypted_file.txt --output decrypted.txt

# Encrypting inside an image
**Encrypting**

- first run: python3.10 key.py *In order to get the key*

**Choose a password of your choice**

- python3.10 run.py --encrypt --password nasa9717 --input Death.jpg  --output Death_encryption.jpg --file njoga.txt *This will produce a new image that contains the data in it*

**Decryption**
- python3.10 run.py --decrypt --password nasa9717 --input Death_encryption.jpg --output njoga_decrypted.txt


# Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files 
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request


## Known Bugs

- ## NONE ##

### License
This application uses:

*MIT*
Copyright (c) 2023 h4ck3r9717

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

