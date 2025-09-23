from flask import jsonify, request, g
from app.database import get_user_by_email
from .utils import create_token
from functools import wraps
from .errors import missing_field_error, invalid_credentials
from werkzeug.security import generate_password_hash, check_password_hash
import jwt, os

ADMIN_EMAIL = os.environ.get("ADMIN_USEREMAIL")
ADMIN_PASS  = os.environ.get("ADMIN_PASSWORD")
JWT_SECRET = os.environ.get("JWT_SECRET")

def employee_login():
    check_login_data = check_login()
    if check_login_data:
        return check_login_data

    data = request.json
    email = data.get("useremail")
    password = data.get("password")

    print("email: ", email)
    print("password: ", password)

    user = get_user_by_email(email)

    if not user or not check_password_hash(user.password, password):
        return invalid_credentials()

    token = create_token(user.user_email, "employee")
    return jsonify({"token": token})

def admin_login():
    check_login_data = check_login()
    if check_login_data:
        return check_login_data

    data = request.json
    email = data.get("useremail")
    password = data.get("password")

    if(email != ADMIN_EMAIL or password != ADMIN_PASS):
        return jsonify({"error": "Invalid credentials"}), 401

    token = create_token("admin", "admin")
    return jsonify({"token": token})


# Middleware that checks the role

def check_role(role):
    """
    Middleware to check if the user has the required role.
    """
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            token = request.headers.get("token")
            if not token:
                return jsonify({"error": "Invalid token"}), 401
            try:
                data = jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
            except jwt.ExpiredSignatureError:
                return jsonify({"error": "Expired token"}), 401
            except:
                return jsonify({"error": "Invalid token"}), 401
            if data["role"] != role:
                return jsonify({"error": "Invalid role"}), 401
            g.token_email = data["email"]
            return fn(*args, **kwargs)
        return wrapper
    return decorator

# Helper function, used as middleware to validate login forms
def check_login():
    # Validate body
    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()

    # Validate params
    required_params = ["useremail", "password"]
    for field in required_params:
        if not data.get(field):
            return missing_field_error(field)

    return False