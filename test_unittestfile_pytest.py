import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_account_registration_success(client):
    json_data = {
        "userID": "004",
        "username" : "username",
        "password" : "password",
        "email" : "email@email.com",
        "role" : "member"
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 200
    assert response.json['message'] == 'User registered successfully'
