from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import bcrypt
import uuid
from flask_jwt_extended import JWTManager, create_access_token
from bracket import Bracket

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True, allow_headers=["Content-Type", "Authorization"], methods=["GET", "POST", "OPTIONS"])


# JWT secret key for user auth
app.config['JWT_SECRET_KEY'] = 'my_jwt_secret_key'
jwt = JWTManager(app)

# config for the railway database
DB_CONFIG = {
    "user": "root",
    "password": "miKyzuiAhcgWWfObFMUPFcXEzCexUzbX",
    "host": "tramway.proxy.rlwy.net",
    "port": 51041,
    "database": "railway",
}

#app route for the register page
@app.route('/register', methods=['POST'])

#register_user() - the function on the /register page for a user to register into the BracketMaster system
#userID - the identifier (primary key) for the member
#username - the name of the user account
#password - the password designated to the user account
#email - the email account that belongs to the user
#role - the designated permissions for when a user is registered (always will be set to member)

def register_user():
    data = request.json  # frontend data

    userID = str(uuid.uuid4())  # generating a unique id for every user
    username = data.get("username")
    password = data.get("password")
    email = data.get("email")
    role = 'member' # default role, set as member for now

    # check if everything is provided (all fields submitted)
    if not username or not password or not email:
        return jsonify({"error": "Missing required fields"}), 400
    
    #checking if a username already exists
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM user WHERE username = %s", (username,))
        if cursor.fetchone():
            return jsonify({"error": "Username already exists"}), 409
    except mysql.connector.Error as err:
        return jsonify({"error": f"Database error: {err}"}), 500
    finally:
        cursor.close()
        conn.close()
    
    #checking if the length of the username is 21 or more characters
    if len(username) >= 21:
        return jsonify({"error": "Username is too many characters"}), 410
    
    #checking if the length of the username is 5 or less characters
    if len(username) <= 5:
        return jsonify({"error": "Username has too few characters"}), 411
    
    #checking if a character in username is a special character
    for i in username:
        if not i.isalnum():
            return jsonify({"error": "Username contains a special character"}), 412
    
    #checking if the length of the password is 21 or more characters
    if len(password) >= 21:
        return jsonify({"error": "Password contains too many characters"}), 413
    
    #checking if the length of the password is 5 or less characters
    if len(password) <= 5:
        return jsonify({"error": "Password contains too few characters"}), 414
    
    #checking if the password contains an uppercase character
    #pass_up_counter - counter used to determine if there is an uppercase character in password, set to true when one is found
    pass_up_counter = False
    for i in password:
        if i.isupper():
            pass_up_counter = True
    if pass_up_counter is False:
        return jsonify({"error": "Password does not contain an uppercase character"}), 415
    
    #checking if the password contains a special character
    #pass_up_counter - counter used to determine if there is a special character in password, set to true when one is found
    pass_spec_char_counter = False
    for i in password:
        if not i.isalnum():
            pass_spec_char_counter = True
    if pass_spec_char_counter is False:
        return jsonify({"error": "Password does not contain a special character"}), 416
    
    #checking if an email already exists
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        cursor.execute("SELECT username FROM user WHERE email = %s", (email,))
        if cursor.fetchone():
            return jsonify({"error": "Email already exists"}), 417
    except mysql.connector.Error as err:
        return jsonify({"error": f"Database error: {err}"}), 500
    finally:
        cursor.close()
        conn.close()

    #checking if the length of the email is 35 or more characters
    if len(email) >= 35:
        return jsonify({"error": "Email contains too many characters"}), 418
    
    #checking if the length of the email is 10 or less characters
    if len(email) <= 10:
        return jsonify({"error": "Email contains too few characters"}), 419
    
    #checking if the email string is missing the @ or . character
    if not email.__contains__('@') or not email.__contains__('.'):
        return jsonify({"error": "Email missing special @ or . character"}), 420

    # hashing the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # insert the user into the DB, return an error if DB err
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = "INSERT INTO user (userID, username, password, email, role) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (userID, username, hashed_password, email, role))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "User registered successfully"}), 200
    except mysql.connector.Error as err:
        return jsonify({"error": f"Database error: {err}"}), 500


@app.route('/login', methods=['POST'])

#login() - the function on the /login page for a user to login into the BracketMaster system
#email - the email account that belongs to the user
#password - the password designated to the user account

def login():
    data = request.json
    email = data["email"]
    password = data["password"]

    # check if one of the fields for login is missing
    if not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM user WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    #testing if the login credentials are valid
    if user and bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
        access_token = create_access_token(identity={"userID": user["userID"], "role": user["role"]})
        return jsonify({"message": "Login successful", "token": access_token}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401

# API route for creating bracket
@app.route('/api/brackets', methods=['POST'])

#create_bracket() - the function on the /bracket page to allow a user to create a bracket
#bracket_id - the ID of the bracket that is randomly generated
#bracket_name - the name of the bracket
#event_type - the type of event being hosted (gaming, soccer, football, chess, etc)
#bracket_type - the style of the bracket (bracketmaster only supports single elimination)
#user_id - the ID of the admin user that is hosting the bracket

def create_bracket():

    data = request.json
    bracket_id = str(uuid.uuid4())[:20]
    bracket_name = data['bracketName']
    event_type = data['eventType']
    bracket_type = data['bracketType']
    user_id = data['userID']

    #testing if the bracketName already exists in bracket
    conn = mysql.connector.connect(**DB_CONFIG)
    cursor = conn.cursor()
    cursor.execute("SELECT bracketName FROM bracket WHERE bracketName = %s", (bracket_name,))
    if cursor.fetchone():
        return jsonify({"error": "Bracket name already exists"}), 440
    
    cursor.close()
    conn.close()

    try:
        bracket = Bracket()
        result = bracket.createBracket(bracket_id, bracket_name, event_type, bracket_type, user_id)
        return jsonify({"message": "Bracket created successfully"}), 201

    # more debugging stuff, check logs for error if its not getting properly inserted
    except Exception as e:
        print("Error:", str(e)) 
        return jsonify({"error": str(e)}), 500

#page to remove a bracket
@app.route('/api/RemoveBracket', methods=['POST'])
def remove_bracket():
    return

#page to create a team
@app.route('/api/CreateTeam', methods=['POST'])
def create_team():
    return

#page to add/remove team from bracket
@app.route('/api/Add-RemoveTeam', methods=['POST'])
def add_remove_team():
    return

if __name__ == '__main__':
    app.run(debug=True)
