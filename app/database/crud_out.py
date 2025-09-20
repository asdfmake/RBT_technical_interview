from . import User
from .database_setup import SessionLocal
from .models import User

def get_user_by_email_and_password(email: str, password: str):
    session = SessionLocal()
    user = session.query(User).filter_by(user_email=email, password=password).one_or_none()
    session.close()
    return user