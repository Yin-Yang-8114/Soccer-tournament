from data import teams, matches, teams_plasyed
from validations import validate_input, team_exist_validation
from score_calc import update_score,calculate_points
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
        match = create_match(home_team_id, away_team_id, home_goals, away_goals)
        update_score(match)
        return matches.append(match)

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


def standings():
    sorted_teams = sorted(teams, key=lambda x: (x["points"],int(x["goals_for"] -x["goals_against"]),x["goals_for"],x["name"]),reverse=True)
    print("Standings:")
    for team in sorted_teams:
        print(f"ID: {team['id']}, Name: {team['name']}, Points: {team['points']}, Goals For: {team['goals_for']}, Goals Against: {team['goals_against']}")



def show_leading_team():
    if not teams:
        print("No teams available.")
        return
    leading_team = max(teams, key=lambda x: (x["points"], int(x["goals_for"] - x["goals_against"]), x["goals_for"], x["name"]))
    print(f"Leading Team: ID: {leading_team['id']}, Name: {leading_team['name']}, Points: {leading_team['points']}, Goals For: {leading_team['goals_for']}, Goals Against: {leading_team['goals_against']}")


def show_best_attacking_team():
    if not teams:
        print("No teams available.")
        return
    best_attacking_team = max(teams, key=lambda x: x["goals_for"])
    print(f"Best Attacking Team: ID: {best_attacking_team['id']}, Name: {best_attacking_team['name']}, Goals For: {best_attacking_team['goals_for']}")



def show_team_success_rate():
    if not teams:
        print("No teams available.")
        return
    for team in teams:
        if team["played"] > 0:
            success_rate = (team["points"] / (team["played"] *3) * 100)
            print(f"Team: {team['name']}, Success Rate: {success_rate:.2f}%")
        else:
            print(f"Team: {team['name']}, Success Rate: N/A (no matches played)")

def show_teams_without_goals():
    teams_without_goals = [team for team in teams if team["goals_for"] == 0]
    if not teams_without_goals:
        print("All teams have scored goals.")
    else:
        print("Teams without goals:")
        for team in teams_without_goals:
            print(f"ID: {team['id']}, Name: {team['name']}") 

def show_tournament_summary():
    if not matches:
        print("No matches have been played.")
        return
    print("Tournament Summary:")
    for match in matches:
        num_of_teams = len(teams)
        num_of_matches = len(matches)
        num_of_goals = sum(match["home_goals"] + match["away_goals"] for match in matches)
        average_goals_per_match = num_of_goals / num_of_matches if num_of_matches > 0 else 0
        num_of_draws = sum(team["draws"] for team in teams) / 2
        top_team = max(teams, key=lambda x: x["points"])
        print(f"the number of tean that perticepted in the turnament is :{num_of_teams}")
        print(f"the number of mutechs that play in the turnament is: {num_of_matches}")
        print(f" the number of goals in all the turnament is : {num_of_goals}")
        print(f" the average of goals in the game is : {average_goals_per_match}")
        print(f" the number of draws in the turnament is : {num_of_draws}")
        print(f" the team that has the most points is :  {top_team['name']}")