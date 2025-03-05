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

class TeamLocationNotFoundError(Exception):
    """No teams are found for a given location."""
    pass

class TeamNotFoundError(Exception):
    """No teams are found for a given teamID."""
    pass

class BracketNotFoundError(Exception):
    """No teams found in this bracket."""
    pass

class InvalidLocationError(Exception):
    """Invalid location. Needs to be >= 0."""
    pass

class InvalidTypeError(Exception):
    """Invalid Type. Needs to be an int"""
    pass

class NoTeamsFoundInBracketError(Exception):
    """No Teams found for this bracket"""
    pass

# Parent function that houses primitive functions to manipulate the database
class Bracket():

    # Adds an entry to the bracket table essentially creating a tournament 
    def createBracket(self, bracketID=None, bracketName=None, eventType=None, bracketType=None, userID=None):
        
        if bracketID is None or bracketName is None or eventType is None or bracketType is None or userID is None:
            return f"TypeError: At least one value is missing an input"

        bracket_query = """
        INSERT INTO bracket (bracketID, bracketName, eventType, bracketType, userID)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (bracketID, bracketName, eventType, bracketType, userID)

        try: 
            with connectToDatabase() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(bracket_query, values)
                    conn.commit()
            success_message = f"Bracket {bracketName} added successfully."
            print(success_message)
            return success_message
        
        except mysql.connector.IntegrityError as e:
            error_message = f"Error entering bracket: {bracketName}"
            print(error_message)
            return error_message

    # Removes bracket from database table bracket. This also removes any assigned entried in teambracket table
    def deleteBracket(self, bracketName):
        delete_query = """
        DELETE FROM bracket
        WHERE bracketName = %s
        """
        values = (bracketName,)

        with connectToDatabase() as conn:
            with conn.cursor() as cursor:
                cursor.execute(delete_query, values)
                conn.commit()
                
            success_message = f"Bracket {bracketName} deleted successfully."
            print(success_message)
            return success_message
        

    # Adds team into database table team    
    def createTeam(self, teamID=None, teamName=None, teamPlayerCount=None, teamLocation=None, teamLeader=None):
        
        if teamID is None or teamName is None or teamPlayerCount is None or teamLocation is None or teamLeader is None:
            return f"TypeError: At least one value is missing an input"

        insert_query = """
        INSERT INTO team (teamID, teamName, teamPlayerCount, teamLocation, teamLeader)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (teamID, teamName, teamPlayerCount, teamLocation, teamLeader)

        try:
            with connectToDatabase() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(insert_query, values)
                    conn.commit()
            success_message = f"Team {teamName} added successfully."
            print(success_message)
            return success_message
                
        except mysql.connector.IntegrityError as e:
            error_message = f"Error: Team {teamName} is already in team table."
            print(error_message)
            return error_message

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
                
            success_message = f"Team with ID {teamID} deleted successfully."
            print(success_message)
            return success_message

    # Adds team to specific bracket
    def addTeamToBracket(self, teamID=None, bracketID=None):

        if teamID is None or bracketID is None:
            return f"TypeError: At least one value is missing an input"

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
            success_message = f"Team with ID {teamID} now assigned to Bracket Match {bracketID}."
            print(success_message)
            return success_message
        
        except mysql.connector.IntegrityError as e:
            error_message = f"Error: Team {teamID} cannot be added to Bracket {bracketID}."
            print(error_message)
            return error_message

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
            success_message = f"Team with ID {teamID} now removed from Bracket Match {bracketID}."
            print(success_message)
            return success_message 
    
    # Displays all the team participants in the bracket
    def displayTeams(self, bracketID):
        list_query = """
        SELECT t.teamName, t.teamPlayerCount, t.teamLocation
        FROM team t
        JOIN teambracket tb ON t.teamID = tb.teamID
        JOIN bracket b ON tb.bracketID = b.bracketID
        WHERE b.bracketID = %s;
        """
        values = (bracketID,)

        try:
            with connectToDatabase() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(list_query, values)
                    teams = cursor.fetchall()

            if teams:
                success_message = f"Teams in Bracket: {bracketID} found."
                print(success_message)
            
                for team in teams:
                    print(f"Team Name: {team[0]}, Players: {team[1]}, Bracket Number: {team[2]}")

                return success_message
            else:
                raise BracketNotFoundError(f"Error: No teams found with in Bracket ID: {bracketID}")

        except BracketNotFoundError as e:
            error_message = str(e)
            print(error_message)
            return error_message 

    # Assign bracket number for a team
    # Ex. bracket has 2 brackets for 4 teams, 2 teams per bracket so TM01 and TM02 are in bracket 1, etc.
    def assignSingleBracketNumber(self, teamID, teamLocation):
        try: 
            if not type(teamLocation) == type(0):
                raise InvalidTypeError(f"Error: teamLocation : {teamLocation} is not a valid type")             
                
        except InvalidTypeError as e:
            error_message = str(e)
            print(error_message)
            return error_message
        
        try:
            if teamLocation <= 0 or teamLocation > 100:
                raise InvalidLocationError(f"Error: teamLocation : {teamLocation} is not in a valid range")
        except InvalidLocationError as e:
            error_message = str(e)
            print(error_message)
            return error_message
        
        assign_query = """
        UPDATE team
        SET teamLocation = %s
        WHERE teamID = %s;
        """
        values = (teamLocation, teamID,)

        try:
            with connectToDatabase() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(assign_query, values)
                    conn.commit()

            success_message = f"Team with ID {teamID} now assigned to bracket {teamLocation}."
            print(success_message)
            return success_message

        except mysql.connector.IntegrityError as e:
            error_message = f"Error: No team found with id: {teamID}."
            print(error_message)
            return error_message  
        

    # Randomly assigns bracket number to all teams in a specific bracket
    def assignAllBracketNumber(self, bracketID):
        getAllTeams_query = """
        SELECT t.teamID 
        FROM team t
        JOIN teambracket tb ON t.teamID = tb.teamID
        WHERE tb.bracketID = %s
        """
        values = (bracketID,)

        try:
            with connectToDatabase() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(getAllTeams_query, values)
                    teams = cursor.fetchall()
        
                    if teams:
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

                        success_message = f"Teams have been randomly assigned successfully."
                        print(f"Teams have been randomly assigned to {bracket_number - 1} bracket(s).")
                        print(success_message)
                        return success_message 
                    else:       
                        raise NoTeamsFoundInBracketError(f"Error: Either bracket does not exist or no teams found in bracket {bracketID}")
                    
        except mysql.connector.IntegrityError as e:
                error_message = f"Error: No teams in the bracket: {bracketID}."
                print(error_message)
                return error_message  
        
        except NoTeamsFoundInBracketError as e:
                error_message = str(e)
                print(error_message)
                return error_message

    #WAITING FOR FRONT END WORK    
    # Returns all information on specific bracket
    def getBracketInfo(self, bracketID):
        print("placeholder")

    # Returns all information on specific team
    def getTeamInfo(self, teamID=None):

        if teamID is None:
            return f"TypeError: Missing 1 required positional argument: 'teamID'"
        
        get_query = """
        SELECT teamID, teamName, teamPlayerCount, teamLocation, teamLeader
        FROM team
        WHERE teamID = %s
        """
        values = (teamID,)

        try:
            with connectToDatabase() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(get_query, values)
                    team_info = cursor.fetchone() 

            if team_info:
                print(f"Team ID: {team_info[0]}")
                print(f"Team Name: {team_info[1]}")
                print(f"Player Count: {team_info[2]}")
                print(f"Team Location: {team_info[3]}")
                print(f"Team Leader: {team_info[4]}")
            else:
                raise TeamNotFoundError(f"Error: No team found with ID: {teamID}")

            success_message = f"Team displayed successfully."
            print(success_message)
            return success_message 
                
        except TeamNotFoundError as e:
            error_message = str(e)
            print(error_message)
            return error_message  
        

    # Returns only position based on teamID
    def getTeamsBasedOnPosition(self, teamLocation):
        query = """
        SELECT t.teamID
        FROM team t
        JOIN teambracket tb ON t.teamID = tb.teamID
        WHERE t.teamLocation = %s
        LIMIT 2
        """
        
        values = (teamLocation,)

        try: 
            with connectToDatabase() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(query, values)
                    teams = cursor.fetchall()

            if not teams:
                raise TeamLocationNotFoundError(f"No teams found for teamLocation: {teamLocation}.")

            success_message = f"Team displayed based on location successfully."
            print(success_message)
            return [team[0] for team in teams]
        
        except TeamLocationNotFoundError as e:
            error_message = str(e)
            print(error_message)
            return error_message
        
    
    # Return total number of brackets
    def getTotalBrackets(self, bracketID):
        getAllTeams_query = """
        SELECT t.teamID 
        FROM team t
        JOIN teambracket tb ON t.teamID = tb.teamID
        WHERE tb.bracketID = %s
        """
        values = (bracketID,)

        try: 
            with connectToDatabase() as conn:
                with conn.cursor() as cursor:
                    cursor.execute(getAllTeams_query, values)
                    teams = cursor.fetchall()

            if not teams:
                raise BracketNotFoundError(f"Error: No teams found with in Bracket ID: {bracketID}")
            
            print(f"Total brackets for {bracketID} is {len(teams) // 2}")
            return (len(teams) // 2)
        
        except BracketNotFoundError as e:
            error_message = str(e)
            print(error_message)
            return error_message 

