import math


def prepare_text(text):
    """
    Removes spaces and converts text to uppercase.
    """
    text = text.replace(" ", "")
    text = text.upper()
    return text


def get_key_order(key):
    """
    Returns column indices in the order of sorted key characters.
    Handles duplicate letters safely.
    """
    key = key.upper()

    # Pair each character with its index
    indexed_key = []
    for index in range(len(key)):
        indexed_key.append((key[index], index))

    # Sort by character first, then index (for duplicates)
    indexed_key.sort(key=lambda item: (item[0], item[1]))

    # Extract the column order
    key_order = []
    for item in indexed_key:
        key_order.append(item[1])

    return key_order


def create_empty_matrix(rows, cols):
    """
    Creates an empty matrix with given rows and columns.
    """
    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            row.append("")
        matrix.append(row)
    return matrix


def encrypt(plaintext, key):
    plaintext = prepare_text(plaintext)
    key = key.upper()

    columns = len(key)
    rows = math.ceil(len(plaintext) / columns)

    # Pad plaintext with 'X'
    total_length = rows * columns
    while len(plaintext) < total_length:
        plaintext += 'X'

    # Create matrix and fill row-wise
    matrix = create_empty_matrix(rows, columns)

    char_index = 0
    for r in range(rows):
        for c in range(columns):
            matrix[r][c] = plaintext[char_index]
            char_index += 1

    # Get column order based on key
    key_order = get_key_order(key)

    # Read columns in sorted order
    ciphertext = ""
    for col_index in key_order:
        for r in range(rows):
            ciphertext += matrix[r][col_index]

    return ciphertext


def decrypt(ciphertext, key):
    key = key.upper()

    columns = len(key)
    rows = len(ciphertext) // columns

    # Create empty matrix
    matrix = create_empty_matrix(rows, columns)

    # Get column order
    key_order = get_key_order(key)

    # Fill matrix column-wise using ciphertext
    char_index = 0
    for col_index in key_order:
        for r in range(rows):
            matrix[r][col_index] = ciphertext[char_index]
            char_index += 1

    # Read matrix row-wise
    plaintext = ""
    for r in range(rows):
        for c in range(columns):
            plaintext += matrix[r][c]

    # Remove padding 'X'
    while plaintext.endswith('X'):
        plaintext = plaintext[:-1]

    return plaintext


# ----------- MAIN PROGRAM -----------

plaintext = input("Enter Plaintext: ")
key = input("Enter Key: ")

encrypted_text = encrypt(plaintext, key)
print("Ciphertext:", encrypted_text)

decrypted_text = decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)