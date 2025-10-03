# secure_login.py

import hashlib
import getpass

# Predefined users for demonstration purposes
USER_CREDENTIALS = {
    "admin": "81dc9bdb52d04dc20036dbd8313ed055"  # MD5 hash for "1234"
}

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def authenticate(username, password):
    hashed_password = hash_password(password)
    if username in USER_CREDENTIALS and USER_CREDENTIALS[username] == hashed_password:
        return True
    return False

username = input("Enter username: ")
password = getpass.getpass("Enter password: ")  # Secure password input

if authenticate(username, password):
    print("Login successful!")
else:
    print("Access denied!")