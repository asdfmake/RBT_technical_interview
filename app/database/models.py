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
class TotalVacations(Base):
    __tablename__ = "total_vacations"

    user_email = Column(String, nullable=False, primary_key=True)
    total_days = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)

# Used vacations model
class UsedVacations(Base):
    __tablename__ = "used_vacations"

    used_vacation_id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_email = Column(String, nullable=False)
    used_days = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)

Base.metadata.create_all(bind=engine)