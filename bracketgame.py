from bracket import Bracket
import mysql.connector

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

class BracketGame(Bracket):

    def __init__(self):
        self.currentRound = 1

    def startGame(self, bracketID):
        print("Placeholder")

    def nextRound(self):
        print("Placeholder")

    def getRoundWinner(self, teamLocation):
        print("Placeholder")

    def declareWinner(self, teamID):
        print("Placeholder")    


# Test
game = BracketGame()
game.listTeams("BK02")