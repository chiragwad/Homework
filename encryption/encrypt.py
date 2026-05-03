# ============================================================
# File Encryption & Decryption - Simple Demo
# Covers: Symmetric (Fernet) and Asymmetric (RSA)
# ============================================================

import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend


# ─────────────────────────────────────────────────────────────
# STEP 1: Create a sample text file to encrypt
# ─────────────────────────────────────────────────────────────
with open("message.txt", "w") as f:
    f.write("Hello! This is a secret message.\nStudent ID: 12345\nCourse: Cryptography")

print("Created message.txt")
print("Original content:", open("message.txt").read())
print()


# ─────────────────────────────────────────────────────────────
# STEP 2: SYMMETRIC ENCRYPTION using Fernet (AES under the hood)
# ─────────────────────────────────────────────────────────────
print("=" * 50)
print("SYMMETRIC ENCRYPTION")
print("=" * 50)

# Generate a key
sym_key = Fernet.generate_key()
print("Symmetric key:", sym_key)

# Save the key to a file (so we can use it later)
with open("sym_key.key", "wb") as f:
    f.write(sym_key)
print("Key saved to sym_key.key")

# Encrypt the file
fernet = Fernet(sym_key)
original_data = open("message.txt", "rb").read()

start = time.time()
encrypted_data = fernet.encrypt(original_data)
sym_enc_time = time.time() - start

with open("sym_encrypted.bin", "wb") as f:
    f.write(encrypted_data)

print("\nEncrypted data (looks like gibberish):")
print(encrypted_data[:80], "...")

# Decrypt the file
start = time.time()
decrypted_data = fernet.decrypt(encrypted_data)
sym_dec_time = time.time() - start

with open("sym_decrypted.txt", "wb") as f:
    f.write(decrypted_data)

print("\nDecrypted content:", decrypted_data.decode())

# Verify it matches the original
if decrypted_data == original_data:
    print("Verification: SUCCESS - matches original!")
else:
    print("Verification: FAILED!")

print(f"Symmetric encrypt time: {sym_enc_time*1000:.4f} ms")
print(f"Symmetric decrypt time: {sym_dec_time*1000:.4f} ms")


# ─────────────────────────────────────────────────────────────
# STEP 3: ASYMMETRIC ENCRYPTION using RSA
# ─────────────────────────────────────────────────────────────
print()
print("=" * 50)
print("ASYMMETRIC ENCRYPTION (RSA)")
print("=" * 50)

# Generate RSA private and public keys
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = private_key.public_key()
print("RSA key pair generated (2048-bit)")

# Save private key to file
with open("rsa_private.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Save public key to file
with open("rsa_public.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("Private key saved to rsa_private.pem")
print("Public key saved to rsa_public.pem")

# NOTE: RSA can only encrypt small amounts of data (max ~190 bytes for 2048-bit).
# So we encrypt the message directly since it's small enough.
original_data = open("message.txt", "rb").read()

start = time.time()
encrypted_data = public_key.encrypt(
    original_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
rsa_enc_time = time.time() - start

with open("rsa_encrypted.bin", "wb") as f:
    f.write(encrypted_data)

print("\nEncrypted with PUBLIC key (looks like gibberish):")
print(encrypted_data[:80], "...")

# Decrypt using private key
start = time.time()
decrypted_data = private_key.decrypt(
    encrypted_data,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
rsa_dec_time = time.time() - start

with open("rsa_decrypted.txt", "wb") as f:
    f.write(decrypted_data)

print("\nDecrypted with PRIVATE key:", decrypted_data.decode())

if decrypted_data == original_data:
    print("Verification: SUCCESS - matches original!")
else:
    print("Verification: FAILED!")

print(f"RSA encrypt time: {rsa_enc_time*1000:.4f} ms")
print(f"RSA decrypt time: {rsa_dec_time*1000:.4f} ms")


# ─────────────────────────────────────────────────────────────
# STEP 4: PERFORMANCE COMPARISON
# ─────────────────────────────────────────────────────────────
print()
print("=" * 50)
print("PERFORMANCE COMPARISON")
print("=" * 50)
print(f"Symmetric total time : {(sym_enc_time + sym_dec_time)*1000:.4f} ms")
print(f"Asymmetric total time: {(rsa_enc_time + rsa_dec_time)*1000:.4f} ms")