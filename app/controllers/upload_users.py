from flask import jsonify, request
from io import StringIO
from database import create_user
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

    return {"users_added": users}, 201