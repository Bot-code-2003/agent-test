# buggy_login.py

username = input("Enter username: ")
password = input("Enter password: ")

# BAD: direct string comparison without hashing/sanitization
if username == "admin" and password == "1234":
    print("Login successful!")
else:
    print("Access denied!")
