from .database_setup import SessionLocal
from .models import User, UsedVacations
import datetime
from sqlalchemy import and_, or_

def get_user_by_email_and_password(email: str, password: str):
    session = SessionLocal()
    user = session.query(User).filter_by(user_email=email, password=password).one_or_none()
    session.close()
    return user

def get_employee_used_days(employee_email: str, search_start: datetime.date, search_end: datetime.date):
    session = SessionLocal()
    users = session.query(UsedVacations).filter(
        UsedVacations.vacation_start >= search_start,
        UsedVacations.vacation_end <= search_end,
        UsedVacations.user_email == employee_email
    ).all()
    session.close()
    return users