from flask import Flask, request
from controllers import home, upload_users_file, upload_used_vacation_file, upload_vacation_days_file

app = Flask(__name__)

@app.route("/")
def home_route():
    return home()

@app.route("/users/upload", methods=["POST"])
def upload_users_route():
    return upload_users_file()

@app.route("/users/vacations/upload", methods=["POST"])
def upload_used_vacation_route():
    return upload_used_vacation_file()

@app.route("/users/vacations_dates/upload", methods=["POST"])
def upload_vacation_days_file_route():
    return upload_vacation_days_file()


if __name__ == "__main__":
    app.run(debug=True)
