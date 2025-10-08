# secure_login.py
import hashlib

def hash_password(password):
    """Hashes a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Predefined credentials (hashed for security)
stored_username = "admin"
stored_password_hash = hash_password("1234")  # Replace "1234" with a more secure password

# Secure login
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

# Hash the input password and compare securely
if username == stored_username and hash_password(password) == stored_password_hash:
    print("Login successful!")
else:
    print("Access denied!")