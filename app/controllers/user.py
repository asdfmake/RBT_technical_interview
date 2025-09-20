import app.database as database
from flask import jsonify, request

def get_user_used_days():
    employee_email = request.args.get("employee_email")
    vacation_year = request.args.get("year")

    used_vacations_for_user = database.get_employee_used_days(employee_email, vacation_year)
    used_vacations_for_user = [instance.to_dict() for instance in used_vacations_for_user]

    used_days = sum(vacation["days_on_vacation"] for vacation in used_vacations_for_user)
    return jsonify({"days on vacation": used_days}), 200