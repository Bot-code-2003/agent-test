# secure_login.py
import hashlib

def hash_password(password):
    """Hash a password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

# Predefined hashed credentials (hashed versions of "admin" and "1234")
PREDEFINED_USERNAME = "admin"
PREDEFINED_PASSWORD_HASH = hash_password("1234")

def authenticate(username, password):
    """Authenticate a user based on username and hashed password."""
    if username == PREDEFINED_USERNAME and hash_password(password) == PREDEFINED_PASSWORD_HASH:
        return True
    return False

username = input("Enter username: ")
password = input("Enter password: ")

if authenticate(username, password):
    print("Login successful!")
else:
    print("Access denied!")