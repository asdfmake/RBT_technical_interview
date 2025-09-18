from .database_setup import SessionLocal
from .models import User 

def create_user(user_email: str, password: str, year: int):
    session = SessionLocal()
    new_user = User(user_email=user_email, password=password, year=year)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    session.close()
    return new_user