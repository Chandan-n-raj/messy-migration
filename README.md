# Messy Migration – Refactored User Management API

## ✅ What I Did

This project started as a legacy Flask API with all logic written in a single file (`app.py`). It had security issues, messy structure, and lacked validation. I refactored the project to make it clean, secure, and maintainable.

### Key Improvements:
- Organized code into separate folders for routing, services, utilities, and DB access.
- Removed SQL injection vulnerabilities by using safe database queries.
- Used password hashing instead of storing plain text passwords.
- Implemented proper input validation and error handling.
- Returned consistent HTTP responses with meaningful status codes.

---

## 🛠️ How to Run

1. Install dependencies from `requirements.txt`
2. Run `init_db.py` to create and populate the database
3. Start the server with `python app.py`

The app will run at `http://localhost:5000`.

---

## 🔬 How I Tested

Using Postman, I tested the following endpoints:

- **Health Check**: `/`
- **Get All Users**: `/users`
- **Get User by ID**: `/user/<id>`
- **Create User**: `/users` (POST)
- **Update User**: `/user/<id>` (PUT)
- **Delete User**: `/user/<id>` (DELETE)
- **Login**: `/login`
- **Search Users**: `/search?name=<name>`

Each endpoint was tested for:
- Valid and invalid input
- Correct status codes
- Expected results (like creation, deletion, and login response)

---

## ✅ Outcome

The final refactored API is:
- Secure (no SQL injection, hashed passwords)
- Modular and readable
- Easy to extend or test
- Aligned with best practices for small Flask APIs

