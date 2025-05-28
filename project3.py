def caesar_cipher(message, shift, mode='e'):
    result = ""
    for char in message:
        if char.isupper():
            base = ord('A')
            if mode == 'e':
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
        elif char.islower():
            base = ord('a')
            if mode == 'e':
                new_char = chr((ord(char) - base + shift) % 26 + base)
            else:
                new_char = chr((ord(char) - base - shift) % 26 + base)
            result += new_char
        else:
            result += char  # Preserve spaces, punctuation
    return result

# === User Interaction ===
print("=== Caesar Cipher Tool ===")
while True:
    mode = input("Do you want to encrypt or decrypt? (e/d): ").lower()
    if mode in ['e', 'd']:
        break
    print("Please enter 'e' to encrypt or 'd' to decrypt.")

message = input("Enter your message: ")

while True:
    try:
        shift = int(input("Enter the shift amount (1–25): "))
        if 1 <= shift <= 25:
            break
        else:
            print("Please enter a number between 1 and 25.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# === Processing ===
result = caesar_cipher(message, shift, mode)
action = "Encrypted" if mode == 'e' else "Decrypted"
print(f"{action} message:", result)
