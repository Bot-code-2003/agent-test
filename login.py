# secure_login.py

import hashlib

# Securely hashed credentials for demonstration purposes
SECURE_USERNAME = "admin"
SECURE_PASSWORD_HASH = hashlib.sha256("secure_password".encode()).hexdigest()

def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def authenticate(username, password):
    """Authenticate user by securely comparing hashed credentials."""
    hashed_password = hash_password(password)
    return username == SECURE_USERNAME and hashed_password == SECURE_PASSWORD_HASH

# Input from user
username = input("Enter username: ")
password = input("Enter password: ")

if authenticate(username, password):
    print("Login successful!")
else:
    print("Access denied!")