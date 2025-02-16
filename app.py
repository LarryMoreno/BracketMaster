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


@app.route('/register', methods=['POST'])
def register_user():
    data = request.json  # frontend data

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    role = 'member' # default role, set as member for now

    # check if everything is provided (all fields submitted)
    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    # hashing the password
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    # insert the user into the DB, return an error if DB err
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = "INSERT INTO user (username, password, email, role) VALUES (%s, %s, %s, %s)"
        cursor.execute(query, (username, hashed_password, email, role))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "User registered successfully"}), 201
    except mysql.connector.Error as err:
        return jsonify({"error": f"Database error: {err}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
