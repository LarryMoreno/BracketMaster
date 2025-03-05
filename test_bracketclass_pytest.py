import bracket
import bracketgame
from bracket import Bracket

#testing that a bracket can be created
def test_bracket_creation():
    
    bracketID = "BK0001"
    bracketName = "THE Tournament 2.0"
    eventType = "Single Elimination"
    bracketType = "Public"
    userID = "USER001"

    bracket = Bracket()
    result = bracket.createBracket(bracketID, bracketName, eventType, bracketType, userID)
    
    assert result == f"Bracket {bracketName} added successfully."

#testing that a bracket cannot be created when value bracketType is missing input
def test_bracket_creation_no_input1():

    bracketID = "BK24"
    bracketName = "Tournament of Champions"
    eventType = "Single Elimination"
    userID = "USER001"

    bracket = Bracket()
    result = bracket.createBracket(bracketID, bracketName, eventType, userID)
    
    assert result == f"TypeError: At least one value is missing an input"

#testing that a bracket cannot be created when value bracketID is missing input
def test_bracket_creation_no_input2():

    bracketName = "Tournament of Champions"
    eventType = "Single Elimination"
    bracketType = 'Standard'
    userID = "USER001"

    bracket = Bracket()
    result = bracket.createBracket(bracketName, eventType, bracketType, userID)
    
    assert result == f"TypeError: At least one value is missing an input"

#testing that a bracket cannot be created when value bracketName is missing input
def test_bracket_creation_no_input3():

    bracketID = "BK24"
    eventType = "Single Elimination"
    bracketType = 'Standard'
    userID = "USER001"

    bracket = Bracket()
    result = bracket.createBracket(bracketID, eventType, bracketType, userID)
    
    assert result == f"TypeError: At least one value is missing an input"

#testing that a bracket cannot be created when value eventType is missing input
def test_bracket_creation_no_input4():

    bracketID = "BK24"
    bracketName = 'New Tournament'
    bracketType = 'Standard'
    userID = "USER001"

    bracket = Bracket()
    result = bracket.createBracket(bracketID, bracketName, bracketType, userID)
    
    assert result == f"TypeError: At least one value is missing an input"

#testing that a bracket cannot be created when value userID is missing input
def test_bracket_creation_no_input5():

    bracketID = "BK24"
    bracketName = 'New Tournament'
    eventType = 'Single Elimination'
    bracketType = 'Standard'

    bracket = Bracket()
    result = bracket.createBracket(bracketID, bracketName, eventType, bracketType)
    
    assert result == f"TypeError: At least one value is missing an input"

#testing that a bracket cannot be created where a bracket already exists
def test_bracket_creation_already_exists():
    
    bracketID = "BK00"
    bracketName = "Tournament 2025"
    eventType = "Single Elimination"
    bracketType = "Public"
    userID = "USER001"

    bracket = Bracket()
    result = bracket.createBracket(bracketID, bracketName, eventType, bracketType, userID)
    
    assert result == f"Error entering bracket: {bracketName}"

#testing that a bracket can be deleted
def test_bracket_deletion():
    
    bracketName = 'TestBracket'

    bracket = Bracket()
    result = bracket.deleteBracket(bracketName)
    
    assert result == f"Bracket {bracketName} deleted successfully."

#testing that a team can be created
def test_team_creation():

    teamID = 'T001'
    teamName = 'FourPF'
    teamPlayerCount = '10'
    teamLocation = 5
    teamLeader = 'Yours Truly'

    bracket = Bracket()
    result = bracket.createTeam(teamID, teamName, teamPlayerCount, teamLocation, teamLeader)

    assert result == f"Team {teamName} added successfully."

#testing that a team cannot be created when teamID is missing input
def test_team_creation_no_input1():

    teamName = 'FourPF'
    teamPlayerCount = '10'
    teamLocation = 5
    teamLeader = 'Yours Truly'

    bracket = Bracket()
    result = bracket.createTeam(teamName, teamPlayerCount, teamLocation, teamLeader)

    assert result == f"TypeError: At least one value is missing an input"

#testing that a team cannot be created when teamName is missing input
def test_team_creation_no_input2():

    teamID = 'T001'
    teamPlayerCount = '10'
    teamLocation = 5
    teamLeader = 'Yours Truly'

    bracket = Bracket()
    result = bracket.createTeam(teamID, teamPlayerCount, teamLocation, teamLeader)

    assert result == f"TypeError: At least one value is missing an input"

#testing that a team cannot be created when teamPlayerCount is missing input
def test_team_creation_no_input3():

    teamID = 'T001'
    teamName = 'FourPF'
    teamLocation = 5
    teamLeader = 'Yours Truly'

    bracket = Bracket()
    result = bracket.createTeam(teamID, teamName, teamLocation, teamLeader)

    assert result == f"TypeError: At least one value is missing an input"

#testing that a team cannot be created when teamLocation is missing input
def test_team_creation_no_input4():

    teamID = 'T001'
    teamName = 'FourPF'
    teamPlayerCount = '10'
    teamLeader = 'Yours Truly'

    bracket = Bracket()
    result = bracket.createTeam(teamID, teamName, teamPlayerCount, teamLeader)

    assert result == f"TypeError: At least one value is missing an input"

#testing that a team cannot be created when teamLeader is missing input
def test_team_creation_no_input5():

    teamID = 'T001'
    teamName = 'FourPF'
    teamPlayerCount = '10'
    teamLocation = 5

    bracket = Bracket()
    result = bracket.createTeam(teamID, teamName, teamPlayerCount, teamLocation)

    assert result == f"TypeError: At least one value is missing an input"

#testing that a team cannot be created that already exists
def test_team_creation_already_exists():

    teamID = 'T001'
    teamName = 'FourPF'
    teamPlayerCount = '10'
    teamLocation = 5
    teamLeader = 'Yours Truly'

    bracket = Bracket()
    result = bracket.createTeam(teamID, teamName, teamPlayerCount, teamLocation, teamLeader)

    assert result == f"Error: Team {teamName} is already in team table."

#testing that a team can be deleted
def test_delete_team():

    teamID = 'T001'

    bracket = Bracket()
    result = bracket.deleteTeam(teamID)

    assert result == f"Team with ID {teamID} deleted successfully."

#testing that a team can be added to a bracket
def test_add_team_to_bracket():

    teamID = 'TM08'
    bracketID = 'BK01'

    bracket = Bracket()
    result = bracket.addTeamToBracket(teamID, bracketID)

    assert result == f"Team with ID {teamID} now assigned to Bracket Match {bracketID}."

#testing that a team cannot be added to a bracket where the teamID input is not given
def test_add_team_to_bracket_no_input1():

    bracketID = 'BK01'

    bracket = Bracket()
    result = bracket.addTeamToBracket(bracketID)

    assert result == f"TypeError: At least one value is missing an input"

#testing that a team cannot be added to a bracket where the bracketID input is not given
def test_add_team_to_bracket_no_input2():

    teamID = 'TM08'

    bracket = Bracket()
    result = bracket.addTeamToBracket(teamID)

    assert result == f"TypeError: At least one value is missing an input"

#testing that a team cannot be added to a bracket where the team does not exist
def test_add_team_non_existent_bracket():

    teamID = 'NOTTEAM'
    bracketID = 'BK01'

    bracket = Bracket()
    result = bracket.addTeamToBracket(teamID, bracketID)

    assert result == f"Error: Team {teamID} cannot be added to Bracket {bracketID}."

#testing that a team cannot be added to a bracket where the bracket does not exist
def test_add_team_bracket_non_existent():

    teamID = 'TM08'
    bracketID = 'NOTBRACKET'

    bracket = Bracket()
    result = bracket.addTeamToBracket(teamID, bracketID)

    assert result == f"Error: Team {teamID} cannot be added to Bracket {bracketID}."

 #testing that a team already apart of a bracket cannot be added again to the same bracket
def test_add_team_to_bracket_already_exists():

    teamID = 'TM08'
    bracketID = 'BK01'

    bracket = Bracket()
    result = bracket.addTeamToBracket(teamID, bracketID)

    assert result == f"Error: Team {teamID} cannot be added to Bracket {bracketID}." 

#testing that a team can be removed from a bracket
def test_remove_team_from_bracket():

    teamID = 'TM08'
    bracketID = 'BK01'

    bracket = Bracket()
    result = bracket.removeTeamFromBracket(teamID, bracketID)

    assert result == f"Team with ID {teamID} now removed from Bracket Match {bracketID}."

#testing that teams can be displayed from an input bracket
def test_display_teams_bracket():

    bracketID = 'BK02'

    bracket = Bracket()
    result = bracket.displayTeams(bracketID)

    assert result == f"Teams in Bracket: {bracketID} found."

#testing that teams will not be displayed from an input bracket where the bracket does not exist
def test_display_teams_bracket_non_existent():

    bracketID = 'YAY'

    bracket = Bracket()
    result = bracket.displayTeams(bracketID)

    assert result == f"Error: No teams found with in Bracket ID: {bracketID}"

#testing that a team can be assigned a place number
def test_team_placement_number():

    teamID = 'TM05'
    teamLocation = 4
    
    bracket = Bracket()
    result = bracket.assignSingleBracketNumber(teamID, teamLocation)

    assert result == f"Team with ID {teamID} now assigned to bracket {teamLocation}."

#testing that a team cannot be given an input teamLocation that is not an int
def test_team_placement_number_invalid_type():

    teamID = 'TM02'
    teamLocation = 'a'
    
    bracket = Bracket()
    result = bracket.assignSingleBracketNumber(teamID, teamLocation)

    assert result == f"Error: teamLocation : {teamLocation} is not a valid type"

#testing that a team placement cannot be at the lower boundary of 0
def test_team_placement_number_invalid_range_lower():

    teamID = 'TM02'
    teamLocation = 0
    
    bracket = Bracket()
    result = bracket.assignSingleBracketNumber(teamID, teamLocation)

    assert result == f"Error: teamLocation : {teamLocation} is not in a valid range"

#testing that a team placement cannot be at the upper boundary of 101
def test_team_placement_number_invalid_range_upper():

    teamID = 'TM02'
    teamLocation = 101
    
    bracket = Bracket()
    result = bracket.assignSingleBracketNumber(teamID, teamLocation)

    assert result == f"Error: teamLocation : {teamLocation} is not in a valid range"

#testing that team placement numbers can be randomly assigned
def test_all_team_placement_numbers():

    bracketID = 'BK01'

    bracket = Bracket()
    result = bracket.assignAllBracketNumber(bracketID)

    assert result == f"Error: Either bracket does not exist or no teams found in bracket {bracketID}"

#testing that team placement numbers cannot be randomly assigned to a bracket that does not exist
def test_all_team_placement_numbers_bracket_non_existent():

    bracketID = 'womp'

    bracket = Bracket()
    result = bracket.assignAllBracketNumber(bracketID)

    assert result == f"Error: Either bracket does not exist or no teams found in bracket {bracketID}"

#testing that team placement numbers cannot be randomly assigned to a bracket with no teams
def test_all_team_placement_numbers_bracket_no_teams():

    bracketID = 'BK11'

    bracket = Bracket()
    result = bracket.assignAllBracketNumber(bracketID)

    assert result == f"Error: Either bracket does not exist or no teams found in bracket {bracketID}"

#testing that the team info for a given team is displayed
def test_team_info():

    teamID = 'TM04'

    bracket = Bracket()
    result = bracket.getTeamInfo(teamID)

    assert result == f"Team displayed successfully."

#testing that the team info for a given team is not displayed for a team that does not exist
def test_team_info_non_existent():

    teamID = 'SIKE'

    bracket = Bracket()
    result = bracket.getTeamInfo(teamID)

    assert result == f"Error: No team found with ID: {teamID}"

#testing that the team info for a given team is not displayed for a team received no input
def test_team_info_no_input():

    bracket = Bracket()
    result = bracket.getTeamInfo()

    assert result == f"TypeError: Missing 1 required positional argument: 'teamID'"

# #testing that the positions of a team are returned
# def test_team_position():

#     teamLocation = '1'

#     bracket = Bracket()
#     result = bracket.getTeamsBasedOnPosition(teamLocation)

#     assert result == [team[0] for team in teams]