# secure_login.py

import hashlib

def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Simulated user database
user_db = {
    "admin": hash_password("securepassword123")  # Replace with a strong password
}

# User input
username = input("Enter username: ")
password = input("Enter password: ")

# Hash the input password for comparison
hashed_password = hash_password(password)

# Authentication check
if username in user_db and user_db[username] == hashed_password:
    print("Login successful!")
else:
    print("Access denied!")

# Note: For real applications, use a secure database and implement rate limiting.