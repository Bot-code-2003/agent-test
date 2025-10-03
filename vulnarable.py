import sqlite3
from flask import Flask, request, make_response, redirect

app = Flask(__name__)
app.config["DEBUG"] = True  # SECURITY MISCONFIGURATION: debug enabled

DB = "small.db"

def init_db():
    db = sqlite3.connect(DB)
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)")
    # plaintext password inserted on purpose
    try:
        cur.execute("INSERT INTO users (username, password) VALUES ('bob', 'secret123')")
        db.commit()
    except Exception:
        pass
    db.close()

def get_db():
    return sqlite3.connect(DB)

@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # INJECTION: vulnerable to SQL injection because username is interpolated directly
    q = f"SELECT id, password FROM users WHERE username = '{username}'"
    cur = get_db().cursor()
    cur.execute(q)
    row = cur.fetchone()
    if not row:
        return "Unknown user", 401

    user_id, stored_password = row

    # CRYPTOGRAPHIC FAILURES: comparing plaintext passwords (no hashing)
    if password != stored_password:
        return "Bad credentials", 403

    # BROKEN ACCESS CONTROL / AUTH: trivial unsigned cookie used as session token
    resp = make_response(redirect("/welcome"))
    resp.set_cookie("session", str(user_id))  # predictable, no HttpOnly/Secure flags
    return resp

@app.route("/welcome")
def welcome():
    sid = request.cookies.get("session")
    if not sid:
        return redirect("/login_page")
    # NO validation: user can set any cookie value and access this page
    return f"Hello user id {sid} (insecure session!)"

if __name__ == "__main__":
    init_db()
    app.run(port=5002)
