import app.database as database
from flask import jsonify, request, g
import datetime
from .errors import missing_params_error, missing_field_error, wrong_date_format
from .utils import get_days_on_vacation
from app.database import create_used_vacations


def get_user_used_days():
    """
    Get the number of vacation days used by the authenticated user within a specified date range.
    """
    required_params = ["search_start", "search_end"]
    for param in required_params:
        if not request.args.get(param):
            return missing_params_error(param)

    employee_email = g.token_email
    search_start = datetime.datetime.strptime(request.args.get("search_start"), "%Y-%m-%d")
    search_end = datetime.datetime.strptime(request.args.get("search_end"), "%Y-%m-%d")

    used_days = database.get_employee_used_days(employee_email, search_start, search_end)

    return jsonify({"days on vacation": used_days}), 200

def get_user_vacations_total_days():
    """
    Get the total number of vacation days allocated to the authenticated user for a specified year.
    """
    if not request.args.get("year"):
        return missing_params_error("year")

    employee_email = g.token_email
    year = request.args.get("year")

    return jsonify({"total days": database.get_employee_total_days_for_year(employee_email, year)}), 200

def get_user_available_vacation_days():
    """
    Get the number of available vacation days for the authenticated user for a specified year.
    """
    if not request.args.get("year"):
        return missing_params_error("year")

    employee_email = g.token_email
    year = request.args.get("year")

    available_days = database.get_employee_available_days_for_year(employee_email, year)

    return jsonify({"available_days": available_days}), 200

    # total days for year - used days

def user_register_vacation():
    employee_email = g.token_email

    if not request.is_json:
        return jsonify({"error": "Missing JSON in request"}), 400

    data = request.get_json()

    required_params = ["vacation_start", "vacation_end"]
    for field in required_params:
        if not data.get(field):
            return missing_field_error(field)

    try:
        vacation_start = datetime.datetime.strptime(data['vacation_start'], "%A, %B %d, %Y")
        vacation_end = datetime.datetime.strptime(data['vacation_end'], "%A, %B %d, %Y")
        year = vacation_start.year
    except ValueError:
        return wrong_date_format()

    days_on_vacation = get_days_on_vacation(data["vacation_start"], data["vacation_end"])['days_on_vacation']

    number_of_available_days = database.get_employee_available_days_for_year(employee_email, year)

    if(days_on_vacation > number_of_available_days):
        return jsonify({"error": f"Too many requested days, available vacation days: {number_of_available_days}"}), 400

    used_vacation = create_used_vacations(user_email=employee_email, vacation_start=vacation_start, vacation_end=vacation_end, days_on_vacation=days_on_vacation, year=year).to_dict()

    return jsonify({"insert_id": used_vacation["used_vacation_id"]}), 200
