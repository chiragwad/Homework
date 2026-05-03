def encrypt(plaintext, key):
    ciphertext = ""

    for char in plaintext:
        if char.isalpha():
            # Determine base (uppercase or lowercase)
            base = ord('A') if char.isupper() else ord('a')
            
            # Apply encryption formula: C = (P + k) mod 26
            encrypted_char = chr((ord(char) - base + key) % 26 + base)
            ciphertext += encrypted_char
        else:
            # Preserve spaces and special characters
            ciphertext += char

    return ciphertext


def decrypt(ciphertext, key):
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            
            # Apply decryption formula: P = (C - k) mod 26
            decrypted_char = chr((ord(char) - base - key) % 26 + base)
            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext


# ---- Main Program ----
plaintext = input("Enter plaintext: ")
key = int(input("Enter key (0-25): "))

if 0 <= key <= 25:
    ciphertext = encrypt(plaintext, key)
    decrypted_text = decrypt(ciphertext, key)

    print("\n--- Results ---")
    print("Plaintext: ", plaintext)
    print("Ciphertext:", ciphertext)
    print("Decrypted: ", decrypted_text)
else:
    print("Invalid key! Please enter a value between 0 and 25.")