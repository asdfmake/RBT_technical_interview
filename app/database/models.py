from sqlalchemy import create_engine, Column, String, Integer
from .database_setup import Base, engine
import uuid

# User model
class User(Base):
    __tablename__ = "users"

    userid = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    year = Column(Integer, nullable=False)


# Total vacations model
class AvailableVacationDays(Base):
    __tablename__ = "available_vacation_days"

    vacation_day_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_email = Column(String, nullable=False)
    total_days = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)

# Used vacations model
class UsedVacations(Base):
    __tablename__ = "used_vacations"

    used_vacation_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_email = Column(String, nullable=False)
    vacation_start = Column(String, nullable=False)
    vacation_end = Column(String, nullable=False)
    days_on_vacation = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)

Base.metadata.create_all(bind=engine)