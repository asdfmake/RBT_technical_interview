import jwt, datetime, os

JWT_SECRET = os.getenv("JWT_SECRET")

def get_days_on_vacation(start_date: str, end_date: str):
    start = datetime.datetime.strptime(start_date, "%A, %B %d, %Y")
    end = datetime.datetime.strptime(end_date, "%A, %B %d, %Y")
    delta = end - start
    year = end.year
    return {
        "days_on_vacation": delta.days + 1,
        "year": year,
    }

def create_token(user_email, role):
    payload = {
        "email": user_email,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm="HS256")
    return token

