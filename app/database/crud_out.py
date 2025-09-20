from .database_setup import SessionLocal
from .models import User, UsedVacations

def get_user_by_email_and_password(email: str, password: str):
    session = SessionLocal()
    user = session.query(User).filter_by(user_email=email, password=password).one_or_none()
    session.close()
    return user

def get_employee_used_days(employee_email: str, year: int):
    session = SessionLocal()
    users = session.query(UsedVacations).filter_by(user_email=employee_email, year=year).all()
    session.close()
    return users