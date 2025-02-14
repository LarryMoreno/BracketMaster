from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import bcrypt
from main import SQL_INSERT

app = Flask(__name__)
CORS(app)  # Allows frontend (React) to communicate with backend (Flask)

# API route to handle user registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json  # Get JSON data from frontend

    #what gets inserted into the connection
    userID = '004'
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")
    role = 'member'

    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    #SQL Connection Function Call
    SQL_INSERT(userID, username, hashed_password, email, role)

if __name__ == '__main__':
    app.run(debug=True)
