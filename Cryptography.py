import random
import time

def encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    for i in range(len(plaintext)):
        character = plaintext[i]
        ciphertext += character
        for j in range(key):
            ciphertext += random.choice(alphabet)
    return ciphertext

def decrypt(ciphertext, key):
    # The decryption process removes the random characters added during encryption
    # by skipping every (key + 1)th character in the ciphertext.
    plaintext = ciphertext[0::key + 1]
    return plaintext

# Main program
def main():
    print("Welcome to the Encryption/Decryption program!")

    while True:
        print("\nMenu:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plaintext = input("\nEnter a message to encrypt: ")
            key = int(input("Input a key as a number between 1 and 10: "))
            while not (1 <= key <= 10):
                print("Invalid key, try again!")
                key = int(input("Input a key as a number between 1 and 10: "))

            print("\nEncrypting plaintext...")
            time.sleep(1)
            ciphertext = encrypt(plaintext, key)
            print("\nCiphertext:")
            print(ciphertext)

        elif choice == '2':
            ciphertext = input("\nEnter a message to decrypt: ")
            key = int(input("Input the key used for encryption: "))
            while not (1 <= key <= 10):
                print("Invalid key, try again!")
                key = int(input("Input the key as a number between 1 and 10: "))

            print("\nDecrypting ciphertext...")
            time.sleep(1)
            plaintext = decrypt(ciphertext, key)
            print("\nDecrypted plaintext:")
            print(plaintext)

        elif choice == '3':
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
