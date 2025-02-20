import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

#testing that an account can be created on the system
def test_account_registration_success(client):
    json_data = {
        "userID": "007",
        "username" : "newnewuser",
        "password" : "password",
        "email" : "email@email.com",
        "role" : "member"
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 200
    assert response.json['message'] == 'User registered successfully'

#testing that an account cannot be created where a username already exists
def test_account_creation_username_exists(client):
    json_data = {
        "userID": "007",
        "username" : "newnewuser",
        "password" : "password",
        "email" : "email@email.com",
        "role" : "member"
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 409
    assert response.json['error'] == 'Username already exists'
