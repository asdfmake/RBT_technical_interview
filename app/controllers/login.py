from flask import jsonify, request
from app.database import get_user_by_email_and_password
from .utils import create_token
from functools import wraps
import jwt, os

ADMIN_EMAIL = os.environ.get("ADMIN_USEREMAIL")
ADMIN_PASS  = os.environ.get("ADMIN_PASSWORD")

def employee_login():
    data = request.json
    email = data.get("useremail")
    password = data.get("password")

    user = get_user_by_email_and_password(email, password)

    if not user or not user.password:
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_token(user, "employee")
    return jsonify({"token": token})

def admin_login():
    data = request.json
    email = data.get("useremail")
    password = data.get("password")

    if(email != ADMIN_EMAIL or password != ADMIN_PASS):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_token("admin", "admin")
    return jsonify({"token": token})


# Middleware that checks the role

def check_role(role):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            # token = request.headers.get("token")
            # data = jwt.decode(token, "hardcoded", algorithms=["HS256"])
            print(role)
            return fn(*args, **kwargs)
        return wrapper
    return decorator