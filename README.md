# Cryptography

# Encryption and Decryption Program

This Python program allows users to encrypt and decrypt messages using a basic encryption algorithm. It offers an interactive interface where users can input messages, choose encryption keys, and see the encrypted or decrypted output.

## Features

- **Encryption**:
  - Encrypts a message using a basic algorithm that adds random characters between each original character based on a chosen key.
  - Key must be a number between 1 and 10.

- **Decryption**:
  - Decrypts a previously encrypted message using the same key.
  - Recovers the original plaintext from the ciphertext by removing the added random characters.

## Usage

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/encryption-decryption.git
   cd encryption-decryption
   ```

2. **Run the program**:

   ```bash
   python encryption_decryption.py
   ```

3. **Follow the prompts**:
   - Choose option 1 to encrypt a message.
   - Enter a message and choose a key (1 to 10) for encryption.
   - The program will display the encrypted ciphertext.
   
   - Choose option 2 to decrypt a message.
   - Enter the encrypted ciphertext and the key used for encryption.
   - The program will display the decrypted plaintext.

4. **Exit the program**:
   - Choose option 3 to exit the program.

## Example

```plaintext
Welcome to the Encryption/Decryption program!

Menu:
1. Encrypt a message
2. Decrypt a message
3. Exit
Enter your choice (1/2/3): 1

Enter a message to encrypt: Hello World
Input a key as a number between 1 and 10: 3

Encrypting plaintext...
...
Ciphertext:
HeslJmlmcEoalvZrojnlVd

Menu:
1. Encrypt a message
2. Decrypt a message
3. Exit
Enter your choice (1/2/3): 2

Enter a message to decrypt: HeslJmlmcEoalvZrojnlVd
Input the key used for encryption: 3

Decrypting ciphertext...
...
Decrypted plaintext:
Hello World

Menu:
1. Encrypt a message
2. Decrypt a message
3. Exit
Enter your choice (1/2/3): 3

Exiting the program. Goodbye!
```

### Notes:

- Ensure Python 3.x is installed on your system to run the program.
- Modify the encryption algorithm or add additional security measures based on specific requirements.
- Contributions and feedback are welcome! Feel free to fork the repository and submit pull requests.
