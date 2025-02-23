import mysql.connector

# db config
DB_CONFIG = {
    "user": "root", 
    "password": "miKyzuiAhcgWWfObFMUPFcXEzCexUzbX",
    "host": "tramway.proxy.rlwy.net",
    "port": 51041,
    "database": "railway",
}

conn = mysql.connector.connect(**DB_CONFIG)
cursor = conn.cursor()


insert_query = """
    INSERT INTO user (userID, username, password, email, role)
    VALUES (%s, %s, %s, %s, %s)
"""
values = ('USER001', 'admin', 'password123', 'admin@example.com', 'admin')


#Actual Bracket Entire
insert_query2 = """
    INSERT INTO bracket (bracketID, bracketName, eventType, bracketType, userID)
    VALUES (%s, %s, %s, %s, %s)
"""
values2 = ('BK02', 'The Second Tournament', 'Single Elimination', 'Knockout', 'USER001')



#Insert teams into team table
insert_query3 = """
    INSERT INTO team (teamID, teamName, teamPlayerCount, teamLocation, teamLeader)
    VALUES (%s, %s, %s, %s, %s)
"""
values3 = ('TM08', 'Torch', '2', '0', 'Four01K')

#Insert teams into team bracket
insert_query4 = """
    INSERT INTO teambracket (bracketID, teamID)
    VALUES (%s, %s)
"""
values4 = ('BK02', 'TM04')


assign_query = """
        UPDATE team
        SET teamLocation = %s
        WHERE teamID = %s;
        """
values5 = (2, 'TM04')

# Execute the query
cursor.execute(insert_query4, values4)

conn.commit()
cursor.execute("SELECT * FROM bracket")
print (cursor.fetchall())
print("-------------------------------------")
cursor.execute("SELECT * FROM team")
print (cursor.fetchall())
print("-------------------------------------")
cursor.execute("SELECT * FROM teambracket")
print (cursor.fetchall())
cursor.close()
conn.close()