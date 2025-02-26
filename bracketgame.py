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

    # Constructor initate instance of round variable
    def __init__(self):
        self.currentRound = 1

    # Runs the game process until winner is found
    def startGame(self, bracketID):
        total = self.getTotalBrackets(bracketID) 

        if total > 0 and (total & (total - 1)) == 0:
            print(f"{total} Valid number of teams")
        else:
            print(f"{total} Invalid number  of teams")
            return
        
        self.assignAllBracketNumber(bracketID)

        while(total >  0):
            print("------------------------------------")
            print(f"ROUND {self.currentRound}")
            self.nextRound(bracketID)
            total = self.getTotalBrackets(bracketID)

    # Manages moving/removing teams to next round until winner is found
    def nextRound(self, bracketID):
        total = self.getTotalBrackets(bracketID) 

        if(total > 1):
            newPos = 1
            for i in range(0, total, 2):
                winner1 = self.getRoundWinner(i+1, bracketID)
                winner2 = self.getRoundWinner(i+2, bracketID)
                self.assignSingleBracketNumber(winner1, newPos)
                self.assignSingleBracketNumber(winner2, newPos)
                newPos += 1
        else:
            finalWinner = self.getRoundWinner(1, bracketID)
            self.declareWinner(finalWinner) 

        self.currentRound+= 1

    # Gets winner from individual bracket
    def getRoundWinner(self, teamLocation, bracketID):
        bracket = self.getTeamsBasedOnPosition(teamLocation)

        #Temporary logic to randomly decide winner
        winner = random.choice(bracket)

        bracket.remove(winner) 
        loser = bracket[0] if bracket else None  

        if loser:
            self.removeTeamFromBracket(loser, bracketID)

        return winner

    # Prints winner to screen
    def declareWinner(self, teamID):
        print("***********************************")
        print("Final Winner: ")
        self.getTeamInfo(teamID)
        print("***********************************")

