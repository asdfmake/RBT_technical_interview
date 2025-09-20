from flask import jsonify, request
from app.database import get_user_by_email_and_password
import jwt
import datetime

def employee_login():
    data = request.json
    email = data.get("useremail")
    password = data.get("password")

    user = get_user_by_email_and_password(email, password)

    if not user or not user.password:
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_token(user, "employee")
    return jsonify({"token": token})

def create_token(user, role):
    payload = {
        "email": user.user_email,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, "hardcoded", algorithm="HS256")
    return token