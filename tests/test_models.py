import datetime
from mixer.backend.sqlalchemy import Mixer
from app.database.models import User, AvailableVacationDays, UsedVacations

mixer = Mixer()


def test_user_model():
    """Test creating a User model instance with Mixer."""
    user = mixer.blend(User, user_email="test@example.com", password="secret", year=2025)

    assert isinstance(user, User)
    assert user.user_email == "test@example.com"
    assert user.password == "secret"
    assert user.year == 2025
    assert user.userid is not None


def test_available_vacation_days_model():
    """Test creating an AvailableVacationDays model instance with Mixer."""
    avd = mixer.blend(
        AvailableVacationDays,
        user_email="test@example.com",
        total_days=20,
        year=2025,
    )

    assert isinstance(avd, AvailableVacationDays)
    assert avd.user_email == "test@example.com"
    assert avd.total_days == 20
    assert avd.year == 2025
    assert avd.vacation_day_id is not None


def test_used_vacations_model():
    """Test creating a UsedVacations model instance with Mixer."""
    start_date = datetime.date(2025, 6, 1)
    end_date = datetime.date(2025, 6, 10)

    used = mixer.blend(
        UsedVacations,
        user_email="test@example.com",
        vacation_start=start_date,
        vacation_end=end_date,
        days_on_vacation=10,
        year=2025,
    )

    assert isinstance(used, UsedVacations)
    assert used.user_email == "test@example.com"
    assert used.vacation_start == start_date
    assert used.vacation_end == end_date
    assert used.days_on_vacation == 10
    assert used.year == 2025
    assert used.used_vacation_id is not None

    # proveri to_dict metodu
    d = used.to_dict()
    assert d["user_email"] == "test@example.com"
    assert d["days_on_vacation"] == 10
