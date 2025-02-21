import mysql.connector
import random

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


class Bracket():
    bracket_list = []
    #self.bracket_list = [[] for _ in range(2)]
    
    #Adds an entry to the bracket table essentially creating a tournament 
    def createBracket(self, bracketID, bracketName, eventType, bracketType, userID):
        bracket_query = """
        INSERT INTO team (bracketID, bracketName, eventType, bracketType, userID)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (bracketID, bracketName, eventType, bracketType, userID)

        cursor.execute(bracket_query, values)
        conn.commit()

        print(f"Bracket {bracketName} added successfully.")

    #Adds team into database table team    
    def createTeam(self, teamID, teamName, teamPlayerCount, teamLocation, teamLeader):
        insert_query = """
        INSERT INTO team (teamID, teamName, teamPlayerCount, teamLocation, teamLeader)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (teamID, teamName, teamPlayerCount, teamLocation, teamLeader)

        cursor.execute(insert_query, values)
        conn.commit()

        print(f"Team {teamName} added successfully.")

    #Removes team from database table team     
    def deleteTeam(self, teamID):
        delete_query = """
        DELETE FROM team
        WHERE teamID = %s
        """
        values = (teamID,)

        cursor.execute(delete_query, values)
        conn.commit()

        print(f"Team with ID {teamID} deleted successfully.")

    #Displays all the team participants in the bracket
    def listTeams(self, bracketID):
        list_query = """
        SELECT t.teamName, t.teamPlayerCount, t.teamLocation
        FROM team t
        JOIN teambracket tb ON t.teamID = tb.teamID
        JOIN bracket b ON tb.bracketID = b.bracketID
        WHERE b.bracketID = %s;
        """
        values = (bracketID,)

        cursor.execute(list_query, values)
        teams = cursor.fetchall()
        print("Teams in Bracket:", bracketID)
        for team in teams:
            print(f"Team Name: {team[0]}, Players: {team[1]}, Bracket Number: {team[2]}")

    #Assign bracket number
    #Ex. bracket has 2 brackets for 4 teams, 2 teams per bracket so TM01 and TM02 are in bracket 1, etc.
    def assignSingleBracketNumber(self, teamLocation, teamID):
        assign_query = """
        UPDATE team
        SET teamLocation = %s
        WHERE teamID = %s;
        """
        values = (teamLocation, teamID,)

        cursor.execute(assign_query, values)

        print(f"Team with ID {teamID} now assigned to bracket {teamLocation}.")

    #Randomly assigns bracket number to all teams
    def assignAllBracketNumber(self, bracketID):
        getAllTeams_query = """
        SELECT t.teamID 
        FROM team t
        JOIN teambracket tb ON t.teamID = tb.teamID
        WHERE tb.bracketID = %s
        """
        values = (bracketID,)
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
        print(f"Teams have been randomly assigned to {bracket_number - 1} brackets.")

    #Adds team to specific bracket
    def addTeamToBracket(self, teamID, bracketID):
        team_query = """
        INSERT INTO teambracket (teamID, bracketID)
        """
        values = (teamID, bracketID)

        cursor.execute(team_query, values)

        print(f"Team with ID {teamID} now assigned to Bracket Match {bracketID}.")

    def removeBracket(self, bracketID):
        delete_query = """
        DELETE FROM bracket
        WHERE bracketID = %s
        """
        values = (bracketID,)

        cursor.execute(delete_query, values)
        conn.commit()

        print(f"Bracket with ID {bracketID} deleted successfully.")

    #
    # The below functions are from an original idea of the bracket class
    # These should not be used, they are just a reference for future functions developed
    #

        
    def moveTeamForward(self):
        #Update position in database
        print("Team moved forward.")

    def removeTeamFromBracket(self, team):
        for bracket in self.bracket_list:
            if team in bracket:
                bracket.remove(team)
                print(f"Team {team} removed from bracket.")
                break 
        
    def placeTeams(self):
        team_index = 0
        for bracket in self.bracket_list:
            if team_index < len(self.team_list) - 1:
                bracket.append(self.team_list[team_index])
                bracket.append(self.team_list[team_index + 1])
                team_index += 2 
        if team_index < len(self.team_list):
            print(f"Remaining teams: {self.team_list[team_index:]}")   
    

# Tesiting around with functions
game = Bracket()

#game.listTeams('BK01')
#game.assignAllBracketNumber('BK01')
game.listTeams('BK01')

print("-----------------------------------")

game.removeBracket("BK01")