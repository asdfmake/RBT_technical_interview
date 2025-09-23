from sqlalchemy import Column, String, Integer, Date
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
    vacation_start = Column(Date, nullable=False)
    vacation_end = Column(Date, nullable=False)
    days_on_vacation = Column(Integer, nullable=False)
    year = Column(Integer, nullable=False)

    def to_dict(self):
        return {
            "used_vacation_id": self.used_vacation_id,
            "user_email": self.user_email,
            "vacation_start": self.vacation_start,
            "vacation_end": self.vacation_end,
            "days_on_vacation": self.days_on_vacation,
            "year": self.year
        }