import hashlib
import json
import os

# ─────────────────────────────────────────────────────────────
# Helper function to compute SHA-512 hash of a file
# ─────────────────────────────────────────────────────────────
def get_hash(filename):
    with open(filename, "rb") as f:
        return hashlib.sha512(f.read()).hexdigest()


# ─────────────────────────────────────────────────────────────
# STEP 1: Create a file and store its original hash
# ─────────────────────────────────────────────────────────────
with open("file.txt", "w") as f:
    f.write("Hello! This is a sample file.\nStudent ID: 12345\nCourse: Cryptography")

original_hash = get_hash("file.txt")

# Save the hash to a file (simulates storing it for later comparison)
with open("stored_hash.txt", "w") as f:
    f.write(original_hash)

print("File created: file.txt")
print("Original hash stored in stored_hash.txt")
print()
print("Original SHA-512 Hash:")
print(original_hash)
print()


# ─────────────────────────────────────────────────────────────
# STEP 2: Check integrity WITHOUT modifying the file
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("CHECK 1: File not modified")
print("=" * 60)

stored_hash = open("stored_hash.txt").read()
current_hash = get_hash("file.txt")

print("Stored Hash :", stored_hash[:60], "...")
print("Current Hash:", current_hash[:60], "...")
print()

if current_hash == stored_hash:
    print("Result: Integrity Verified ✔")
else:
    print("Result: Integrity Compromised ✘")


# ─────────────────────────────────────────────────────────────
# STEP 3: Modify the file and recheck integrity
# ─────────────────────────────────────────────────────────────
print()
print("=" * 60)
print("CHECK 2: File modified")
print("=" * 60)

with open("file.txt", "a") as f:
    f.write("\nThis line was secretly added!")  # tamper with the file

print("File has been modified!")
print()

current_hash = get_hash("file.txt")

print("Stored Hash :", stored_hash[:60], "...")
print("Current Hash:", current_hash[:60], "...")
print()

if current_hash == stored_hash:
    print("Result: Integrity Verified ✔")
else:
    print("Result: Integrity Compromised ✘")