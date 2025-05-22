from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_register_success():
    response = client.post("/register", data={
        "name": "Martin",
        "password": "Abcde1",
        "email": "martin@example.com",
        "birthdate": "2000-01-01",
        "agreed": "true"
    })
    assert response.status_code == 200
    assert response.json()["success"] is True

def test_register_invalid_email():
    response = client.post("/register", data={
        "name": "Martin",
        "password": "Abcde1",
        "email": "martinexample.com",
        "birthdate": "2000-01-01",
        "agreed": "true"
    })
    assert response.status_code == 200
    assert response.json()["success"] is False
    assert "email" in response.json()["message"].lower()