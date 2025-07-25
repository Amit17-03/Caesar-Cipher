def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase separately
            base = ord('A') if char.isupper() else ord('a')
            shifted = (ord(char) - base + shift) % 26 + base
            result += chr(shifted)
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher ===")
    choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").strip().upper()

    if choice not in ['E', 'D']:
        print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (integer): "))
    except ValueError:
        print("Invalid shift value. Please enter an integer.")
        return

    if choice == 'E':
        encrypted = caesar_encrypt(message, shift)
        print(f"Encrypted message: {encrypted}")
    else:
        decrypted = caesar_decrypt(message, shift)
        print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()
