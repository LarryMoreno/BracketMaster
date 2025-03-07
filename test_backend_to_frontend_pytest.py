import pytest
import bracket
import bracketgame
from bracket import Bracket
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

#testing that an account cannot be created where a username contains 21 or more characters
def test_account_registration_username_too_long(client):
    json_data = {
        "username" : "abcdefghijklmnopqrstu",
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

#testing that an account cannot be created where a password contains 21 or more characters
def test_account_registration_password_too_long(client):
    json_data = {
        "username" : "newuser1",
        "password" : "Thississapassssword!!",
        "email" : "cemail3@amail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 413
    assert response.json['error'] == 'Password contains too many characters'

#testing that an account can be created where a password contains 20 characters
def test_account_registration_password_upper_boundary(client):
    json_data = {
        "username" : "newuser1",
        "password" : "Thississapasssword!!",
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

#testing that an account cannot be created where an email contains 10 or less characters
def test_account_registration_email_too_short(client):
    json_data = {
        "username" : "newuser5",
        "password" : "Testt!",
        "email" : "a@mail.com",
    }

    response = client.post('/register', json=json_data)

    assert response.status_code == 419
    assert response.json['error'] == 'Email contains too few characters'

#testing that an account can be created where an email contains 11 characters
def test_account_registration_email_lower_boundary(client):
    json_data = {
        "username" : "newuser5",
        "password" : "Testt!",
        "email" : "ab@gmail.com",
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

#testing that an account cannot be signed into that does not exist
def test_account_login_email_does_not_exist(client):
    json_data = {
        "email" : "cooljohnguy@gmail.com",
        "password" : "IamJohn@27",
    }

    response = client.post('/login', json=json_data)

    assert response.status_code == 401
    assert response.json['error'] == 'Invalid email or password'

#testing that a bracket can be created
def test_bracket_creation(client):
    json_data = {
        
        'bracketName' : 'appTes',
        'eventType' : 'anothertestgang',
        'bracketType' : 'Single Elimination',
        'userID' : 'USER001',
    }
    response = client.post('/api/brackets', json=json_data)

    assert response.status_code == 201
    assert response.json['message'] == "Bracket created successfully"

#testing that a bracket cannot be created as the bracket already exists
def test_bracket_creation_already_exists(client):
    json_data = {
        'bracketName' : 'appTest',
        'eventType' : 'anothertestgang',
        'bracketType' : 'Single Elimination',
        'userID' : 'USER001',
    }
    response = client.post('/api/brackets', json=json_data)

    assert response.status_code == 440
    assert response.json['error'] == "Bracket name already exists"

#testing that a team can be created and added to a bracket
def test_team_creation_bracket_add(client):
    json_data ={
        'teamName' : 'CAMelss',
        'teamPlayerCount' : '4',
        'teamLocation' : '1',
        'teamLeader' : 'Carlos',
        'bracketID' : 'BK12'
    }
    response = client.post('/api/create-team', json=json_data)

    assert response.status_code == 202
    assert response.json['message'] == "Team successfuly created and added to bracket"

#testing that a team cannot be added to a bracket where the team is already in the bracket
def test_team_creation_bracket_add_team_in_bracket(client):
    json_data ={
        'teamName' : 'CamelsS',
        'teamPlayerCount' : '4',
        'teamLocation' : '1',
        'teamLeader' : 'Carlos',
        'bracketID' : 'BK13'
    }
    response = client.post('/api/create-team', json=json_data)

    assert response.status_code == 441
    assert response.json['error'] == "Team already exists in bracket"

#testing that a team cannot be added to a bracket that does not exist
def test_team_creation_bracket_add_no_bracket(client):
    json_data ={
        'teamName' : 'Camels 2.0',
        'teamPlayerCount' : '4',
        'teamLocation' : '1',
        'teamLeader' : 'Carlos',
        'bracketID' : 'BK-1'
    }
    response = client.post('/api/create-team', json=json_data)

    assert response.status_code == 442
    assert response.json['error'] == "BracketID entered does not exist"

#testing that a bracket can be deleted
def test_bracket_delete(client):
    json_data = {
        'bracketID' : 'BK10'
    }
    response = client.post('/api/remove-bracket', json=json_data)

    assert response.status_code == 203
    assert response.json['message'] == 'Bracket successfully deleted'

#testing that a bracket cannot be deleted if the bracketID does not exist
def test_bracket_delete_non_existent(client):
    json_data = {
        'bracketID' : 'testing',
    }
    response = client.post('/api/remove-bracket', json=json_data)

    assert response.status_code == 443
    assert response.json['error'] == 'BracketID entered does not exist'

#testing that a team can be removed from a bracket
def test_remove_team_bracket(client):
    json_data = {
        'bracketID' : 'BK02',
        'teamID' : 'TM08',
    }
    response = client.post('/api/remove-team', json=json_data)

    assert response.status_code == 204
    assert response.json['message'] == 'Team successfully removed from bracket'