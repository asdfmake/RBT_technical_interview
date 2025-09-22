from flask import Flask, request
from app.controllers import home, upload_users_file, upload_used_vacation_file, upload_vacation_days_file, employee_login, admin_login, check_role, get_user_used_days, get_user_available_vacation_days, get_user_vacations_total_days, user_register_vacation
import sys, os
from dotenv import load_dotenv
app = Flask(__name__)

@app.route("/")
def home_route():
    return home()

@app.route("/admin/upload/users_list", methods=["POST"])
@check_role("admin")
def upload_users_route():
    return upload_users_file()

@app.route("/admin/upload/used_vacation", methods=["POST"])
@check_role("admin")
def upload_used_vacation_route():
    return upload_used_vacation_file()

@app.route("/admin/upload/vacation_days", methods=["POST"])
@check_role("admin")
def upload_vacation_days_file_route():
    return upload_vacation_days_file()

@app.route("/login/employee", methods=["POST"])
def login_employee_route():
    return employee_login()

@app.route("/login/admin", methods=["POST"])
def login_admin_route():
    return admin_login()

@app.route("/employee/get_used_days", methods=["GET"])
@check_role("employee")
def get_user_used_days_route():
    return get_user_used_days()

@app.route("/employee/get_available_vacation_days", methods=["GET"])
@check_role("employee")
def get_user_available_vacation_days_route():
    return get_user_available_vacation_days()

@app.route("/employee/get_total_days", methods=["GET"])
@check_role("employee")
def get_total_days_route():
    return get_user_vacations_total_days()

@app.route("/employee/register_new_vacation", methods=["POST"])
@check_role("employee")
def user_register_vacation_route():
    return user_register_vacation()

load_dotenv()

required_env_vars = ["DATABASE_URL", "ADMIN_USEREMAIL", "ADMIN_PASSWORD", "JWT_SECRET"]
missing_vars = [var for var in required_env_vars if not os.getenv(var)]

if missing_vars:
    print(f"ERROR: Missing environment variables: {', '.join(missing_vars)}")
    sys.exit(1)

if __name__ == "__main__":
    app.run(debug=True)
