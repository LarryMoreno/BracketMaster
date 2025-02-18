import mysql.connector

# db config
DB_CONFIG = {
    "user": "root", 
    "password": "miKyzuiAhcgWWfObFMUPFcXEzCexUzbX",
    "host": "tramway.proxy.rlwy.net",
    "port": 51041,
    "database": "railway",
}

# insert
def SQL_INSERT(userID, username, password, email, role):
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        cursor = conn.cursor()
        query = "INSERT INTO user (userID, username, password, email, role) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(query, (userID, username, password, email, role))
        conn.commit()
        cursor.close()
        conn.close()
        return "✅ User inserted successfully."
    except mysql.connector.Error as err:
        #print(f"❌ Database Error: {err}")
        return "Database error"
