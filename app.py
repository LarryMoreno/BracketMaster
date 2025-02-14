from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
import bcrypt

app = Flask(__name__)
CORS(app)  # Allows frontend (React) to communicate with backend (Flask)

# MySQL Connection
db = mysql.connector.connect(
    host="127.0.0.1",
    user="larrymoreno",
    password="your_mysql_password",
    database="collinheaney"
)
cursor = db.cursor()

# API route to handle user registration
@app.route('/register', methods=['POST'])
def register_user():
    data = request.json  # Get JSON data from frontend

    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "Missing required fields"}), 400

    # Hash the password before storing it
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, hashed_password))
        db.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
