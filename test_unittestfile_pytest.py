import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

#testing that an account can be created on the system
def test_account_registration_success(client):
    json_data = {
        "username" : "CollinHeaney",
        "password" : "Password!",
        "email" : "realemail@email.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 200
    assert response.json['message'] == 'User registered successfully'

#testing that an account cannot be created where a username already exists
def test_account_registration_username_exists(client):
    json_data = {
        "username" : "CollinHeaney",
        "password" : "Password!",
        "email" : "legitemail@gmail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 409
    assert response.json['error'] == 'Username already exists'

#testing that an account cannot be created where a username contains 16 or more characters
def test_account_registration_username_too_long(client):
    json_data = {
        "username" : "abcdefghijklmnop",
        "password" : "Password!",
        "email" : "cemail@cmail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 410
    assert response.json['error'] == 'Username is too many characters'

#testing that an account can be created where a username contains 15 characters
def test_account_registration_username_upper_boundary(client):
    json_data = {
        "username" : "123456789123456",
        "password" : "Password!",
        "email" : "cemail@amail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 200
    assert response.json['message'] == 'User registered successfully'

#testing that an account cannot be created where a username contains 5 or less characters
def test_account_registration_username_too_short(client):
    json_data = {
        "username" : "12345",
        "password" : "Password!",
        "email" : "cemail@bmail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 411
    assert response.json['error'] == 'Username has too few characters'

#testing that an account can be created where a username contains 6 characters
def test_account_registration_username_lower_boundary(client):
    json_data = {
        "username" : "sixsix",
        "password" : "Password!",
        "email" : "cemail1@amail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 200
    assert response.json['message'] == 'User registered successfully'

#testing that an account cannot be created where a username contains a special character
def test_account_registration_username_special_charcter(client):
    json_data = {
        "username" : "@@@@@@",
        "password" : "Password!",
        "email" : "cemail2@amail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 412
    assert response.json['error'] == 'Username contains a special character'

#testing that an account cannot be created where a password contains 16 or more characters
def test_account_registration_password_too_long(client):
    json_data = {
        "username" : "newuser1",
        "password" : "Thisisapassword!",
        "email" : "cemail3@amail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 413
    assert response.json['error'] == 'Password contains too many characters'

#testing that an account can be created where a password contains 15 characters
def test_account_registration_password_upper_boundary(client):
    json_data = {
        "username" : "newuser1",
        "password" : "Thisisapasswor!",
        "email" : "ecmail4@amail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 200
    assert response.json['message'] == 'User registered successfully'

#testing that an account cannot be created where a password contains 5 or less characters
def test_account_registration_password_too_short(client):
    json_data = {
        "username" : "newuser2",
        "password" : "Test!",
        "email" : "cemail3@amail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 414
    assert response.json['error'] == 'Password contains too few characters'

#testing that an account can be created where a password contains 6 characters
def test_account_registration_password_lower_boundary(client):
    json_data = {
        "username" : "newuser2",
        "password" : "Testt!",
        "email" : "cemail5@amail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 200
    assert response.json['message'] == 'User registered successfully'

#testing that an account cannot be created where a password does not contain an uppercase character
def test_account_registration_password_no_uppercase(client):
    json_data = {
        "username" : "newuser3",
        "password" : "testt!",
        "email" : "cemail6@amail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 415
    assert response.json['error'] == 'Password does not contain an uppercase character'

#testing that an account cannot be created where a password does not contain a special character
def test_account_registration_password_no_special_char(client):
    json_data = {
        "username" : "newuser3",
        "password" : "Testtt",
        "email" : "cemail6@amail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 416
    assert response.json['error'] == 'Password does not contain a special character'

#testing that an account cannot be created where an email already exists
def test_account_registration_email_already_exists(client):
    json_data = {
        "username" : "newuser3",
        "password" : "Testt!",
        "email" : "cemail1@amail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 417
    assert response.json['error'] == 'Email already exists'

#testing that an account cannot be created where an email contains 35 or more characters
def test_account_registration_email_too_long(client):
    json_data = {
        "username" : "newuser4",
        "password" : "Testt!",
        "email" : "abcdefghijklmnopqrstuvwxyz@mail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 418
    assert response.json['error'] == 'Email contains too many characters'

#testing that an account can be created where an email contains 34 characters
def test_account_registration_email_upper_boundary(client):
    json_data = {
        "username" : "newuser4",
        "password" : "Testt!",
        "email" : "bcdefghijklmnopqrstuvwxyz@mail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 200
    assert response.json['message'] == 'User registered successfully'

#testing that an account cannot be created where an email contains 15 or less characters
def test_account_registration_email_too_short(client):
    json_data = {
        "username" : "newuser5",
        "password" : "Testt!",
        "email" : "abcdef@mail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 419
    assert response.json['error'] == 'Email contains too few characters'

#testing that an account can be created where an email contains 16 characters
def test_account_registration_email_lower_boundary(client):
    json_data = {
        "username" : "newuser5",
        "password" : "Testt!",
        "email" : "abcdef@gmail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 200
    assert response.json['message'] == 'User registered successfully'

#testing that an account cannot be created where an email is missing the @ symbol
def test_account_registration_email_missing_char_a(client):
    json_data = {
        "username" : "newuser6",
        "password" : "Testt!",
        "email" : "abcdefghimail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 420
    assert response.json['error'] == 'Email missing special @ or . character'

#testing that an account cannot be created where an email is missing the @ symbol
def test_account_registration_email_missing_char_dot(client):
    json_data = {
        "username" : "newuser6",
        "password" : "Testt!",
        "email" : "abcdefghi@mailcom",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 420
    assert response.json['error'] == 'Email missing special @ or . character'

