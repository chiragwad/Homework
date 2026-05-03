def decrypt(ciphertext, key):
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            
            # Decryption: P = (C - k) mod 26
            decrypted_char = chr((ord(char) - base - key) % 26 + base)
            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext


# Brute Force Program
ciphertext = input("Enter ciphertext: ")

print("\n--- Brute Force Results ---")
for key in range(26):
    decrypted_text = decrypt(ciphertext, key)
    print(f"Key {key:2}: {decrypted_text}")