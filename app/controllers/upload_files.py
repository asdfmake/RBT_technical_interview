from flask import jsonify, request
from io import StringIO
from app.database import create_user, create_used_vacations, create_available_vacations
from datetime import datetime
import csv

def upload_users_file():
    if "file" not in request.files:
        return {"error": "No file provided"}, 400

    file = request.files["file"]

    if file.filename == "":
        return {"error": "No file selected"}, 400
    
    content = file.read().decode("utf-8")

    vacation_year = int(content.splitlines()[0].split(",")[1]) # get vacation year from first line

    content = "\n".join(content.splitlines()[1:])  # Remove the first line

    csv_file = StringIO(content)

    reader = csv.DictReader(csv_file)
    users = [row for row in reader]

    for user in users:
        create_user(user['Employee Email'], user['Employee Password'], vacation_year)

    return {"users_added": len(users)}, 201

def upload_used_vacation_file():
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
        create_used_vacations(
            uv['Employee'],
            uv['Vacation start date'],
            uv['Vacation end date'],
            days_and_year['days_on_vacation'],
            days_and_year['year']
        )

    return {"Vacations added: ": len(used_vacations)}, 201


# Move this to utils file
def get_days_on_vacation(start_date: str, end_date: str):
    start = datetime.strptime(start_date, "%A, %B %d, %Y")
    end = datetime.strptime(end_date, "%A, %B %d, %Y")
    delta = end - start
    year = end.year
    return {
        "days_on_vacation": delta.days + 1,
        "year": year,
    }

def upload_vacation_days_file():
    if "file" not in request.files:
        return {"error": "No file provided"}, 400

    file = request.files["file"]

    if file.filename == "":
        return {"error": "No file selected"}, 400

    content = file.read().decode("utf-8")

    vacation_year = int(content.splitlines()[0].split(",")[1])  # get vacation year from first line

    content = "\n".join(content.splitlines()[1:])  # Remove the first line

    csv_file = StringIO(content)

    reader = csv.DictReader(csv_file)
    vacation_days = [row for row in reader]

    for d in vacation_days:
        create_available_vacations(d['Employee'], d['Total vacation days'], vacation_year)

    return {"vacation_days added": len(vacation_days)}, 201

