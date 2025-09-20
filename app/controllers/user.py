import app.database as database
from flask import jsonify, request, g
import datetime

def get_user_used_days():
    employee_email = g.token_email
    search_start = datetime.datetime.strptime(request.args.get("search_start"), "%Y-%m-%d")
    search_end = datetime.datetime.strptime(request.args.get("search_end"), "%Y-%m-%d")

    used_days = database.get_employee_used_days(employee_email, search_start, search_end)

    return jsonify({"days on vacation": used_days}), 200

def get_user_vacations_total_days():
    employee_email = g.token_email
    year = request.args.get("year")

    return jsonify({"total days": database.get_employee_total_days_for_year(employee_email, year)}), 200

def get_user_available_vacation_days():
    employee_email = g.token_email
    year = request.args.get("year")

    available_days = database.get_employee_available_days_for_year(employee_email, year)

    return jsonify({"available_days": available_days}), 200

    # total days for year - used days
