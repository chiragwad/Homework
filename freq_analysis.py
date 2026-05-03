from collections import Counter

def decrypt(ciphertext, key):
    plaintext = ""

    for char in ciphertext:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - base - key) % 26 + base)
            plaintext += decrypted_char
        else:
            plaintext += char

    return plaintext


def frequency_analysis(ciphertext):
    # Count only alphabetic characters (case-insensitive)
    filtered = [c.lower() for c in ciphertext if c.isalpha()]
    freq = Counter(filtered)
    return freq


def estimate_key(most_freq_char, assumed_char):
    # Convert to 0–25 index
    c = ord(most_freq_char) - ord('a')
    p = ord(assumed_char) - ord('a')
    
    # key = (C - P) mod 26
    return (c - p) % 26


# ---- Main Program ----
ciphertext = input("Enter ciphertext: ")

# Step 1–2: Frequency count
freq = frequency_analysis(ciphertext)
print("\n--- Frequency Count ---")
for char, count in freq.most_common():
    print(f"{char}: {count}")

# Step 3: Most frequent character
if freq:
    most_freq_char = freq.most_common(1)[0][0]
    print(f"\nMost frequent character: '{most_freq_char}'")

    # Step 3–4: Try mapping to common letters
    common_letters = ['e', 't', 'a']

    print("\n--- Estimated Keys ---")
    estimated_keys = []
    for letter in common_letters:
        key = estimate_key(most_freq_char, letter)
        estimated_keys.append(key)
        print(f"Assuming '{most_freq_char}' -> '{letter}' => Key = {key}")

    # Step 5: Decrypt using estimated keys
    print("\n--- Decryption using Estimated Keys ---")
    for key in estimated_keys:
        print(f"Key {key:2}: {decrypt(ciphertext, key)}")

# Step 6: Compare with brute force
print("\n--- Brute Force Comparison ---")
for key in range(26):
    print(f"Key {key:2}: {decrypt(ciphertext, key)}")