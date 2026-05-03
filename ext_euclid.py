def extended_gcd(a, b):
    # Base Case
    if b == 0:
        return a, 1, 0
    
    # Recursive call
    gcd, x1, y1 = extended_gcd(b, a % b)
    
    # Update x and y using results of recursive call
    x = y1
    y = x1 - (a // b) * y1
    
    return gcd, x, y

if __name__ == "__main__":
    a = 48
    b = 18

    gcd, x, y = extended_gcd(a, b)

    print(f"gcd = {gcd}")
    print(f"x = {x}")
    print(f"y = {y}")

    # Verification
    print(f"Verification: ax + by = {a * x + b * y}")