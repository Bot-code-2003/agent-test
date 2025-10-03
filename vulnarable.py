# vulnerable_login_demo.py
# Run: python vulnerable_login_demo.py
# WARNING: intentionally insecure — for testing only.

from flask import Flask, request, redirect, make_response, g
import sqlite3
import requests  # used unsafely below for avatar fetch (SSRF demonstration)

DATABASE = "insecure_users.db"

app = Flask(__name__)
app.config["DEBUG"] = True  # SECURITY: debug mode enabled

# --- DB setup (stores plaintext passwords) ---
def get_db():
    db = getattr(g, "_db", None)
    if db is None:
        db = g._db = sqlite3.connect(DATABASE)
    return db

def init_db():
    db = sqlite3.connect(DATABASE)
    cur = db.cursor()
    # plaintext password field
    cur.execute(
        "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT, role TEXT)"
    )
    # insert a user (password in cleartext)
    try:
        cur.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", ("alice", "password123", "user"))
        db.commit()
    except Exception:
        pass
    db.close()

# --- Vulnerable login endpoint ---
@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    # INJECTION: unsafely building SQL with string formatting (SQLi)
    # vulnerable_line:
    query = f"SELECT id, username, password, role FROM users WHERE username = '{username}'"
    cur = get_db().cursor()
    cur.execute(query)  # vulnerable to SQL injection if username contains quotes
    row = cur.fetchone()

    if not row:
        return "No such user", 401

    user_id, user_name, stored_password, role = row

    # CRYPTOGRAPHIC FAILURES: comparing plaintext passwords; no hashing/salting
    if password != stored_password:
        return "Invalid credentials", 403

    # IDENTIFICATION & AUTH FAILURES / BROKEN ACCESS CONTROL:
    # - We set a trivial session cookie containing user id (no signing, no HttpOnly/secure flags)
    resp = make_response(redirect("/profile"))
    resp.set_cookie("session_id", str(user_id))  # predictable, unsigned cookie

    # SECURITY MISCONFIGURATION: CORS, cookies not secure, debug True above

    return resp

# --- Profile endpoint (no auth checks, simple cookie-based) ---
@app.route("/profile")
def profile():
    # BROKEN ACCESS CONTROL: no verification of cookie ownership or role checks
    sid = request.cookies.get("session_id")
    if not sid:
        return redirect("/login_page")

    # Insecure: no input validation, treat sid as int without try/except
    cur = get_db().cursor()
    cur.execute(f"SELECT username, role FROM users WHERE id = {sid}")  # SQLi if sid manipulated
    row = cur.fetchone()
    if not row:
        return "Unknown session", 401

    username, role = row

    # SSRF demonstration: user can set ?avatar=<url> and server will fetch it without validation
    avatar_url = request.args.get("avatar")
    avatar_data = None
    if avatar_url:
        try:
            # UNSAFE: server-side request to arbitrary URL (SSRF)
            r = requests.get(avatar_url, timeout=2)
            avatar_data = r.content[:100]  # we just peek at some bytes
        except Exception:
            avatar_data = b"fetch-failed"

    return (
        f"Hello {username} (role={role})\n"
        f"Avatar peek: {bool(avatar_data)}\n"
    )

# --- Admin-only action but no RBAC enforced ---
@app.route("/admin/delete_user", methods=["POST"])
def delete_user():
    # Insecure: trusting 'role' parameter from client (can be spoofed)
    role = request.form.get("role")
    target = request.form.get("username")
    # NO CHECK that current user is an admin
    db = get_db()
    db.cursor().execute("DELETE FROM users WHERE username = ?", (target,))
    db.commit()
    return f"Deleted {target} (requested by role={role})"

if __name__ == "__main__":
    init_db()
    app.run(port=5001)
