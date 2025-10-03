from flask import Flask, request, make_response, redirect
import sqlite3
import hashlib
import os
from flask.sessions import SecureCookieSessionInterface

app = Flask(__name__)
app.config["DEBUG"] = False  # Debug mode disabled for production
app.secret_key = os.urandom(32)  # Strong random secret key for session management

DB = "small.db"

def init_db():
    db = sqlite3.connect(DB)
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)")
    # Passwords are hashed before storing
    try:
        hashed_password = hashlib.sha256("secret123".encode()).hexdigest()
        cur.execute("INSERT INTO users (username, password) VALUES ('bob', ?)", (hashed_password,))
        db.commit()
    except sqlite3.IntegrityError:
        pass
    db.close()

def get_db():
    return sqlite3.connect(DB)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "").strip()
    password = request.form.get("password", "").strip()

    # Using parameterized queries to prevent SQL injection
    cur = get_db().cursor()
    cur.execute("SELECT id, password FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    if not row:
        return "Unknown user", 401

    user_id, stored_password = row

    # Hashing the provided password and comparing it with the stored hash
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if hashed_password != stored_password:
        return "Bad credentials", 403

    # Secure session management
    resp = make_response(redirect("/welcome"))
    resp.set_cookie("session", str(user_id), httponly=True, secure=True)  # HttpOnly and Secure flags added
    return resp

@app.route("/welcome")
def welcome():
    sid = request.cookies.get("session")
    if not sid or not sid.isdigit():  # Validate the session cookie value
        return redirect("/login_page")
    return f"Hello user id {sid} (secure session!)"

if __name__ == "__main__":
    init_db()
    app.run(port=5002)