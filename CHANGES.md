# CHANGES.md

## 🔧 Major Issues Identified
- SQL Injection via string interpolation
- Plaintext password storage
- No input validation
- All code in a single file
- Inconsistent responses and status codes

## ✅ Refactoring Summary
- Split code into models, services, routes, utils
- Used parameterized queries (`?`) to prevent SQL injection
- Used `werkzeug.security` for password hashing
- Added proper status codes and error handling
- Centralized DB connection in `db.py`

## 🤔 Trade-offs
- Still uses SQLite and no ORM for simplicity
- No session/token management (not required)

## 📌 If I Had More Time
- Add unit tests with `pytest`
- Use SQLAlchemy ORM
- Add logging and environment config
