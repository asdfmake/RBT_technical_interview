from .database_setup import SessionLocal
from .models import User, UsedVacations, AvailableVacationDays
import datetime
from sqlalchemy import and_, or_

def get_user_by_email(email: str):
    """
    Fetches a user by email
    returns User object or None
    """
    session = SessionLocal()
    user = session.query(User).filter_by(user_email=email).one_or_none()
    session.close()
    return user

def get_employee_used_days(employee_email: str, search_start: datetime.date, search_end: datetime.date):
    """
    Searches for employee used days by search_start and search_end
    returns integer with used days
    """
    session = SessionLocal()
    users = session.query(UsedVacations).filter(
        UsedVacations.vacation_start >= search_start,
        UsedVacations.vacation_end <= search_end,
        UsedVacations.user_email == employee_email
    ).all()
    session.close()
    users = [instance.to_dict() for instance in users]
    used_days = sum(vacation["days_on_vacation"] for vacation in users)

    return used_days

def get_employee_total_days_for_year(employee_email: str, year: int):
    """
    Fetches total vacation days for an employee for a specific year
    returns integer with total days
    """
    session = SessionLocal()
    total_days = session.query(AvailableVacationDays).filter_by(year=year, user_email=employee_email).one_or_none().total_days
    session.close()
    return total_days

def get_employee_available_days_for_year(employee_email: str, year: int):
    """
    Calculates available vacation days for an employee for a specific year
    returns integer with available days
    """
    total_days = get_employee_total_days_for_year(employee_email, year)

    search_start = datetime.datetime.strptime(f"{year}-1-1", "%Y-%m-%d")
    search_end = datetime.datetime.strptime(f"{year}-12-31", "%Y-%m-%d")

    available_days = total_days - get_employee_used_days(employee_email, search_start, search_end)

    return available_days

