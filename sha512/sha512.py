import hashlib
import hmac

# ─────────────────────────────────────────────────────────────
# STEP 1: Create a sample file
# ─────────────────────────────────────────────────────────────
with open("file.txt", "w") as f:
    f.write("Hello! This is a sample file.\nStudent ID: 12345\nCourse: Cryptography")

print("Created file.txt")
print("Content:", open("file.txt").read())
print()


# ─────────────────────────────────────────────────────────────
# STEP 2: Compute SHA-512 hash of the file
# ─────────────────────────────────────────────────────────────
with open("file.txt", "rb") as f:
    data = f.read()

hash_val = hashlib.sha512(data).hexdigest()

print("=" * 60)
print("ORIGINAL FILE")
print("=" * 60)
print("SHA-512 Hash:")
print(hash_val)
print()


# ─────────────────────────────────────────────────────────────
# STEP 3: Generate a secret key and compute HMAC using SHA-512
# ─────────────────────────────────────────────────────────────
secret_key = b"my_secret_key_123"
hmac_val = hmac.new(secret_key, data, hashlib.sha512).hexdigest()

print("Secret Key:", secret_key)
print()
print("HMAC-SHA512:")
print(hmac_val)
print()


# ─────────────────────────────────────────────────────────────
# STEP 4: Modify the file and recompute hash and HMAC
# ─────────────────────────────────────────────────────────────
with open("file.txt", "a") as f:
    f.write("\nThis line was added!")  # small change to the file

print("=" * 60)
print("AFTER MODIFYING FILE")
print("=" * 60)

with open("file.txt", "rb") as f:
    modified_data = f.read()

new_hash = hashlib.sha512(modified_data).hexdigest()
new_hmac = hmac.new(secret_key, modified_data, hashlib.sha512).hexdigest()

print("New SHA-512 Hash:")
print(new_hash)
print()
print("New HMAC-SHA512:")
print(new_hmac)
print()


# ─────────────────────────────────────────────────────────────
# STEP 5: Compare results
# ─────────────────────────────────────────────────────────────
print("=" * 60)
print("COMPARISON")
print("=" * 60)
print(f"Hash changed : {hash_val != new_hash}")
print(f"HMAC changed : {hmac_val != new_hmac}")
print()
print(f"Original Hash (first 40 chars): {hash_val[:40]}...")
print(f"New Hash     (first 40 chars): {new_hash[:40]}...")
print()
print(f"Original HMAC (first 40 chars): {hmac_val[:40]}...")
print(f"New HMAC      (first 40 chars): {new_hmac[:40]}...")