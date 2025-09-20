from flask import Flask, request
from controllers import home, upload_users_file, upload_used_vacation_file, upload_vacation_days_file, employee_login, admin_login, check_role, get_user_used_days, get_user_available_vacation_days

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
def get_user_used_days_route():
    return get_user_used_days()

@app.route("/employee/get_available_vacation_days", methods=["GET"])
def get_user_available_vacation_days_route():
    return get_user_available_vacation_days()


if __name__ == "__main__":
    app.run(debug=True)
