from data import teams, matches, teams_plasyed
from validations import validate_input, team_exist_validation

def add_much_result():
    while True:
        home_team_id = validate_input("enter home team id: ", "positive_num")
        if  team_exist_validation(val=home_team_id):
            print("team does not exist")
            continue
        away_team_id = validate_input("enter away team id: ", "positive_num")
        if  team_exist_validation(val=away_team_id):
            print("team does not exist")
            continue
        if home_team_id == away_team_id:
            print("home and away team cannot be the same")
            continue
        if home_team_id + away_team_id in (teams_plasyed):
            print("match already played")
            continue
        home_goals = validate_input("enter home team goals: ", "positive_num")
        away_goals = validate_input("enter away team goals: ", "positive_num")
        teams_plasyed.append((home_team_id + away_team_id))
        return matches.append(create_match(home_team_id, away_team_id, home_goals, away_goals))

def create_team(id, name):
    team = {
        "id": id,
        "name": name,
        "played": 0,
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
        "points": 0}
    return team

def create_match(home_team_id, away_team_id, home_goals, away_goals):
    match = {
        "home_team_id": home_team_id,
        "away_team_id": away_team_id,
        "home_goals": home_goals,
        "away_goals": away_goals}
    return match

def show_all_teams():
    if not teams:
        print("No teams available.")
    else:
        for team in teams:
            print(f"ID: {team['id']}, Name: {team['name']}, Played: {team['played']}, Wins: {team['wins']}, Draws: {team['draws']}, Losses: {team['losses']}, Goals For: {team['goals_for']}, Goals Against: {team['goals_against']}, Points: {team['points']}")

def add_team():
    while True:
        name = validate_input("enter team name: ", "str").lower()
        if not team_exist_validation(val=name):
            print("team already exists")
            continue
        id =  validate_input("enter team id: ", "positive_num")
        if not team_exist_validation(val=id):
            print("team id already exists")
            continue
        else:
            return teams.append(create_team(id, name))