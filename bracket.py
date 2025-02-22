import mysql.connector
import random

# DB Configuration
DB_CONFIG = {
    "user": "root", 
    "password": "miKyzuiAhcgWWfObFMUPFcXEzCexUzbX",
    "host": "tramway.proxy.rlwy.net",
    "port": 51041,
    "database": "railway",
}

# Helper function to get connection to database
def connectToDatabase():
    return mysql.connector.connect(**DB_CONFIG)


# Parent function that houses primitive functions to manipulate the database
class Bracket():

    # Adds an entry to the bracket table essentially creating a tournament 
    def createBracket(self, bracketID, bracketName, eventType, bracketType, userID):
        bracket_query = """
        INSERT INTO team (bracketID, bracketName, eventType, bracketType, userID)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (bracketID, bracketName, eventType, bracketType, userID)

        with connectToDatabase() as conn:
            with conn.cursor() as cursor:
                cursor.execute(bracket_query, values)
                conn.commit()

        print(f"Bracket {bracketName} added successfully.")

    # Removes bracket from database table bracket. This also removes any assigned entried in teambracket table
    def deleteBracket(self, bracketID):
        delete_query = """
        DELETE FROM bracket
        WHERE bracketID = %s
        """
        values = (bracketID,)

        with connectToDatabase() as conn:
            with conn.cursor() as cursor:
                cursor.execute(delete_query, values)
                conn.commit()

        print(f"Bracket with ID {bracketID} deleted successfully.")

    # Adds team into database table team    
    def createTeam(self, teamID, teamName, teamPlayerCount, teamLocation, teamLeader):
        insert_query = """
        INSERT INTO team (teamID, teamName, teamPlayerCount, teamLocation, teamLeader)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (teamID, teamName, teamPlayerCount, teamLocation, teamLeader)

        with connectToDatabase() as conn:
            with conn.cursor() as cursor:
                cursor.execute(insert_query, values)
                conn.commit()

        print(f"Team {teamName} added successfully.")

    # Removes team from database table team     
    def deleteTeam(self, teamID):
        delete_query = """
        DELETE FROM team
        WHERE teamID = %s
        """
        values = (teamID,)

        with connectToDatabase() as conn:
            with conn.cursor() as cursor:
                cursor.execute(delete_query, values)
                conn.commit()

        print(f"Team with ID {teamID} deleted successfully.")

    # Adds team to specific bracket
    def addTeamToBracket(self, teamID, bracketID):
        team_query = """
        INSERT INTO teambracket (teamID, bracketID)
        VALUES (%s, %s)
        """
        values = (teamID, bracketID)

        try:
            with connectToDatabase() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(team_query, values)
                    conn.commit()

            print(f"Team with ID {teamID} now assigned to Bracket Match {bracketID}.")

        except mysql.connector.IntegrityError as e:
            print(f"Error: Team {teamID} is already in Bracket {bracketID}.")


    # Removes team from specific bracket
    def removeTeamFromBracket(self, teamID, bracketID):
        remove_query = """
        DELETE FROM teambracket
        WHERE teamID = %s AND bracketID = %s
        """
        values = (teamID, bracketID)

        with connectToDatabase() as conn:
            with conn.cursor() as cursor:
                cursor.execute(remove_query, values)
                conn.commit()

        print(f"Team with ID {teamID} now removed from Bracket Match {bracketID}.")    
    
    # Displays all the team participants in the bracket
    def listTeams(self, bracketID):
        list_query = """
        SELECT t.teamName, t.teamPlayerCount, t.teamLocation
        FROM team t
        JOIN teambracket tb ON t.teamID = tb.teamID
        JOIN bracket b ON tb.bracketID = b.bracketID
        WHERE b.bracketID = %s;
        """
        values = (bracketID,)

        with connectToDatabase() as conn:
            with conn.cursor() as cursor:
                cursor.execute(list_query, values)
                teams = cursor.fetchall()

        print("Teams in Bracket:", bracketID)
        for team in teams:
            print(f"Team Name: {team[0]}, Players: {team[1]}, Bracket Number: {team[2]}")

    # Assign bracket number for a team
    # Ex. bracket has 2 brackets for 4 teams, 2 teams per bracket so TM01 and TM02 are in bracket 1, etc.
    def assignSingleBracketNumber(self, teamLocation, teamID):
        assign_query = """
        UPDATE team
        SET teamLocation = %s
        WHERE teamID = %s;
        """
        values = (teamLocation, teamID,)

        with connectToDatabase() as conn:
            with conn.cursor() as cursor:
                cursor.execute(assign_query, values)
                conn.commit()

        print(f"Team with ID {teamID} now assigned to bracket {teamLocation}.")

    # Randomly assigns bracket number to all teams in a specific bracket
    def assignAllBracketNumber(self, bracketID):
        getAllTeams_query = """
        SELECT t.teamID 
        FROM team t
        JOIN teambracket tb ON t.teamID = tb.teamID
        WHERE tb.bracketID = %s
        """
        values = (bracketID,)

        with connectToDatabase() as conn:
            with conn.cursor() as cursor:
                cursor.execute(getAllTeams_query, values)
                teams = cursor.fetchall()
      
                random.shuffle(teams)
                
                bracket_number = 1 
                for i in range(0, len(teams), 2):
                    team1 = teams[i][0]
                    team2 = teams[i+1][0] if i+1 < len(teams) else None 
                    teamLocation1 = bracket_number
                    teamLocation2 = bracket_number if team2 else None

                    assign_query = """
                    UPDATE team
                    SET teamLocation = %s
                    WHERE teamID = %s;
                    """
                    
                    cursor.execute(assign_query, (teamLocation1, team1))

                    if team2:
                        cursor.execute(assign_query, (teamLocation2, team2))

                    bracket_number += 1

                conn.commit()
        print(f"Teams have been randomly assigned to {bracket_number - 1} bracket(s).")

