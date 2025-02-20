from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import bcrypt

app = Flask(__name__)
CORS(app)

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

    userID = '007'
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

def login():
    data = request.json
    email = data["email"]
    password = data["password"]

    # check if one of the fields for login is missing
    if not email or not password:
        return jsonify({"error": "Missing fields"}), 400

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM User WHERE email = %s", (email,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if user and bcrypt.check_password_hash(user["password"], password):
        access_token = create_access_token(identity={"userID": user["userID"], "role": user["role"]})
        return jsonify({"message": "Login successful", "token": access_token}), 200
    else:
        return jsonify({"error": "Invalid email or password"}), 401


if __name__ == '__main__':
    app.run(debug=True)
