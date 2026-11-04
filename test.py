teams =[{"id":1,"name":"chaim","played":0,"wins":0,"draws":0,"losses":0,"goals_for":0,"goals_against":0,"points":0},{"id":2,"name":"michaek","played":0,"wins":0,"draws":0,"losses":0,"goals_for":0,"goals_against":0,"points":0}]
team ={"id":None,"name":"","played":0,"wins":0,"draws":0,"losses":0,"goals_for":0,"goals_against":0,"points":0} 
matches = []
teams_plasyed = []



def display_menu():
    print("\nWelcome to the Soccer Tournament!")
    print("1. add a team")
    print("2. show all teams")
    print("3. add match result")
    print("4. show standings")
    print("5. show leading team")
    print("6. show best attacing team")
    print("7. show team success rate")
    print("8. show teams without goals")
    print("9. show tornament summary")
    print("10. chack championship potential")
    print("11. exit")





def user_choice():
    while True:
        display_menu()
        choice = input("Enter your choice (1-11): ")
        if choice.isdigit() and 1 <= int(choice) <= 11:
            return int(choice)
        else:
            print("invalid choice. please enter a number between 1 and 11.")


def main():
    while True:
        choice = user_choice()
        match choice:
            case 1:
                add_team()
            case 2:
                show_all_teams()
            case 3:
                add_much_result()
            case 4:
                standings()
            case 5:
                show_leading_team()
            case 6:
                show_best_attacking_team()
            case 7:
                show_team_success_rate()
            case 8:
                show_teams_without_goals()
            case 9:
                show_tournament_summary()
            case 10:
                pass  # check championship potential
            case 11:
                print("goodbye")
                break



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


def team_exist_validation(val):
    if any(team["name"] == val for team in teams):
        return False
    if any(team["id"] == val for team in teams):
        return False
    return True


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

def show_all_teams():
    if not teams:
        print("No teams available.")
    else:
        for team in teams:
            print(f"ID: {team['id']}, Name: {team['name']}, Played: {team['played']}, Wins: {team['wins']}, Draws: {team['draws']}, Losses: {team['losses']}, Goals For: {team['goals_for']}, Goals Against: {team['goals_against']}, Points: {team['points']}")


def validate_input(message, input_type):
    while True:
        user_input = input(message).strip()
        if input_type == "num":
            if user_input.isdigit():
                return int(user_input)
            else:
                print("please enter a number")
        elif input_type == "positive_num":
            if user_input.isdigit() and int(user_input) >= 0:
                return int(user_input)
            else:
                print("please enter a positive number")
        elif input_type == "str":
            if user_input.isalpha():
                return user_input
            else:
                print("please enter a string")
        elif input_type == "not_empty":
            if user_input.strip():
                return user_input
            else:
                print("cant be empty value")


def standings():
    sorted_teams = sorted(teams, key=lambda x: (x["points"],int(x["goals_for"] -x["goals_against"]),x["goals_for"],x["name"]),reverse=True)
    print("Standings:")
    for team in sorted_teams:
        print(f"ID: {team['id']}, Name: {team['name']}, Points: {team['points']}, Goals For: {team['goals_for']}, Goals Against: {team['goals_against']}")

def update_team_stats(team_id, goals_for, goals_against, points):
    for team in teams:
        if team["id"] == team_id:
            team["played"] += 1
            team["goals_for"] += goals_for
            team["goals_against"] += goals_against
            team["points"] += points
            if points == 3:
                team["wins"] += 1
            elif points == 1:
                team["draws"] += 1
            else:
                team["losses"] += 1
            break


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

def create_match(home_team_id, away_team_id, home_goals, away_goals):
    match = {
        "home_team_id": home_team_id,
        "away_team_id": away_team_id,
        "home_goals": home_goals,
        "away_goals": away_goals}
    return match


def update_score(match):
        home_team_id = match["home_team_id"]
        away_team_id = match["away_team_id"]
        home_goals = match["home_goals"]
        away_goals = match["away_goals"]
        home_points, away_points = calculate_points(home_goals, away_goals)
        update_team_stats(home_team_id, home_goals, away_goals, home_points)
        update_team_stats(away_team_id, away_goals, home_goals, away_points)

def calculate_points(home_goals, away_goals):
    if home_goals > away_goals:
        return 3, 0
    elif home_goals < away_goals:
        return 0, 3
    else:
        return 1, 1

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
    teams_without_goals = [team for team in teams if team["goals_for"] == 0 and team["played"] > 0]
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
main()