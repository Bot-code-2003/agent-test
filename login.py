# secure_login.py

import hashlib
import logging

# Configure logging for authentication attempts
logging.basicConfig(level=logging.INFO, filename='auth.log', format='%(asctime)s - %(message)s')

# Securely hashed credentials for comparison
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD_HASH = hashlib.sha256("1234".encode()).hexdigest()

def authenticate_user(username, password):
    # Hash the password provided by the user
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    # Compare securely hashed values
    if username == ADMIN_USERNAME and password_hash == ADMIN_PASSWORD_HASH:
        logging.info(f"Login successful for user: {username}")
        return "Login successful!"
    else:
        logging.warning(f"Access denied for user: {username}")
        return "Access denied!"

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")

# Authenticate user
print(authenticate_user(username, password))