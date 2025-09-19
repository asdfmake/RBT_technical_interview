from .database_setup import SessionLocal
from .models import User, UsedVacations, AvailableVacationDays

def create_user(user_email: str, password: str, year: int):
    session = SessionLocal()
    new_user = User(user_email=user_email, password=password, year=year)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    session.close()
    return new_user

def create_used_vacations(user_email: str, vacation_start: str, vacation_end: str, days_on_vacation: int,  year: int):
    session = SessionLocal()
    new_used_vacation = UsedVacations(user_email=user_email, vacation_start=vacation_start, vacation_end=vacation_end, days_on_vacation=days_on_vacation, year=year)
    session.add(new_used_vacation)
    session.commit()
    session.refresh(new_used_vacation)
    session.close()
    return new_used_vacation

def create_available_vacations(user_email: str, total_days: int, year: int):
    session = SessionLocal()
    new_available_vacation = AvailableVacationDays(user_email=user_email, total_days=total_days, year=year)
    session.add(new_available_vacation)
    session.commit()
    session.refresh(new_available_vacation)
    session.close()
    return new_available_vacation