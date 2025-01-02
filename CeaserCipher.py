def caesar_cipher(text, shift, mode):
    result = ""

    # Normalize the shift to the range of 0-25
    shift = shift % 26

    for char in text:
        if char.isalpha():
            # Calculate ASCII offset based on case
            offset = ord('A') if char.isupper() else ord('a')
            # Encrypt or decrypt the character
            new_char = chr((ord(char) - offset + (shift if mode == 'encrypt' else -shift)) % 26 + offset)
            result += new_char
        else:
            # Leave non-alphabetic characters unchanged
            result += char

    return result

def main():
    print("✨ Welcome to the Caesar Cipher Program ✨")
    print("Secure your messages or decode them effortlessly.\n")

    while True:
        # Get user choice with validation
        while True:
            mode = input("Would you like to (encrypt/decrypt) a message? ").strip().lower()
            if mode in ['encrypt', 'decrypt']:
                break
            print("❌ Invalid choice. Please type 'encrypt' or 'decrypt'.\n")

        # Get the message
        message = input("📩 Enter your message: ")

        # Get the shift value with validation
        while True:
            try:
                shift = int(input("🔢 Enter the shift value (positive or negative): "))
                break
            except ValueError:
                print("❌ Please enter a valid integer for the shift value.\n")

        # Perform encryption or decryption
        result = caesar_cipher(message, shift, mode)
        action = "🔐 Encrypted" if mode == 'encrypt' else "🔓 Decrypted"
        print(f"\n{action} Message: {result}")

        # Ask the user if they want to continue
        cont = input("\n🔄 Would you like to perform another operation? (yes/no): ").strip().lower()
        if cont != 'yes':
            print("\n Thank you for using the Caesar Cipher Program! Have a great day!🌟")
            break

if __name__ == "__main__":
    main()

