# services/user_service.py
from db import get_db
from utils.helpers import hash_password, check_password, is_valid_email
from flask import abort

def get_all_users():
    db = get_db()
    cursor = db.execute("SELECT id, name, email FROM users")
    return [dict(row) for row in cursor.fetchall()]

def get_user_by_id(user_id):
    db = get_db()
    cursor = db.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
    row = cursor.fetchone()
    if row:
        return dict(row)
    abort(404, description="User not found")

def create_user(name, email, password):
    if not (name and email and password):
        abort(400, description="Missing fields")
    if not is_valid_email(email):
        abort(400, description="Invalid email")
    
    db = get_db()
    try:
        db.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
                   (name, email, hash_password(password)))
        db.commit()
    except:
        abort(409, description="Email already exists")
    return {"message": "User created successfully"}

def update_user(user_id, name, email):
    db = get_db()
    db.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
    db.commit()
    return {"message": "User updated"}

def delete_user(user_id):
    db = get_db()
    db.execute("DELETE FROM users WHERE id = ?", (user_id,))
    db.commit()
    return {"message": "User deleted"}

def search_users(name):
    db = get_db()
    cursor = db.execute("SELECT id, name, email FROM users WHERE name LIKE ?", (f"%{name}%",))
    return [dict(row) for row in cursor.fetchall()]

def login(email, password):
    db = get_db()
    cursor = db.execute("SELECT id, password FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    if not row:
        abort(401, description="Invalid credentials")
    if not check_password(password, row["password"]):
        abort(401, description="Invalid credentials")
    return {"status": "success", "user_id": row["id"]}
