from flask import jsonify, request
from io import StringIO
from app.database import create_user, create_used_vacations, create_available_vacations
from .utils import get_days_on_vacation
from werkzeug.security import generate_password_hash
import csv, datetime

def upload_users_file():
    """
    Upload a CSV file containing user information and create users in the database.
    This function encrypts user passwords before storing them.
    """
    if "file" not in request.files:
        return {"error": "No file provided"}, 400

    file = request.files["file"]

    if file.filename == "":
        return {"error": "No file selected"}, 400
    
    content = file.read().decode("utf-8")

    vacation_year = int(content.splitlines()[0].split(",")[1])

    content = "\n".join(content.splitlines()[1:])

    csv_file = StringIO(content)

    reader = csv.DictReader(csv_file)
    users = [row for row in reader]

    for user in users:
        create_user(user['Employee Email'], generate_password_hash(user['Employee Password']), vacation_year)

    return {"users_added": len(users)}, 201

def upload_used_vacation_file():
    """
    Upload a CSV file containing used vacation information and create used vacation records in the database.
    Before uploading rows, it calculates the number of days on vacation and separates year.
    """
    if "file" not in request.files:
        return {"error": "No file provided"}, 400

    file = request.files["file"]

    if file.filename == "":
        return {"error": "No file selected"}, 400
    
    content = file.read().decode("utf-8")

    csv_file = StringIO(content)

    reader = csv.DictReader(csv_file)
    used_vacations = [row for row in reader]

    for uv in used_vacations:
        days_and_year = get_days_on_vacation(uv['Vacation start date'], uv['Vacation end date'])
        start = datetime.datetime.strptime(uv['Vacation start date'], "%A, %B %d, %Y").date()
        end = datetime.datetime.strptime(uv['Vacation end date'], "%A, %B %d, %Y").date()
        create_used_vacations(
            uv['Employee'],
            start,
            end,
            days_and_year['days_on_vacation'],
            days_and_year['year']
        )

    return {"Vacations added: ": len(used_vacations)}, 201

def upload_vacation_days_file():
    """
    Upload a CSV file containing available vacation days information and create available vacation records in the database.
    Before uploading rows, it separates year from the first line of the file and stores it separately.
    """
    if "file" not in request.files:
        return {"error": "No file provided"}, 400

    file = request.files["file"]

    if file.filename == "":
        return {"error": "No file selected"}, 400

    content = file.read().decode("utf-8")

    vacation_year = int(content.splitlines()[0].split(",")[1])

    content = "\n".join(content.splitlines()[1:])

    csv_file = StringIO(content)

    reader = csv.DictReader(csv_file)
    vacation_days = [row for row in reader]

    for d in vacation_days:
        create_available_vacations(d['Employee'], d['Total vacation days'], vacation_year)

    return {"vacation_days added": len(vacation_days)}, 201

