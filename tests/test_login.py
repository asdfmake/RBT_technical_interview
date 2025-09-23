import pytest
from werkzeug.security import generate_password_hash

from app.controllers import login


@pytest.fixture
def app(monkeypatch):
    from flask import Flask

    app = Flask(__name__)
    app.add_url_rule("/login/employee", view_func=login.employee_login, methods=["POST"])
    app.add_url_rule("/login/admin", view_func=login.admin_login, methods=["POST"])

    # patch env varijable za admina
    monkeypatch.setattr(login, "ADMIN_EMAIL", "admin@example.com")
    monkeypatch.setattr(login, "ADMIN_PASS", "adminpass")
    monkeypatch.setattr(login, "JWT_SECRET", "testsecret")

    return app


@pytest.fixture
def client(app):
    return app.test_client()

def test_employee_login_success(monkeypatch, client):
    # fake user
    class DummyUser:
        def __init__(self):
            self.user_email = "employee@example.com"
            self.password = generate_password_hash("secret")

    monkeypatch.setattr(login, "get_user_by_email", lambda email: DummyUser())
    monkeypatch.setattr(login, "create_token", lambda email, role: "faketoken")

    response = client.post("/login/employee", json={"useremail": "employee@example.com", "password": "secret"})
    assert response.status_code == 200
    assert response.get_json()["token"] == "faketoken"


def test_admin_login_success(monkeypatch, client):
    monkeypatch.setattr(login, "create_token", lambda email, role: "admintoken")

    response = client.post("/login/admin", json={"useremail": "admin@example.com", "password": "adminpass"})
    assert response.status_code == 200
    assert response.get_json()["token"] == "admintoken"