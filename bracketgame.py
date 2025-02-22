from bracket import Bracket
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

class BracketGame(Bracket):

    def placeholder():
        print("Placeholder")


# Test
game = BracketGame()
game.listTeams("BK02")