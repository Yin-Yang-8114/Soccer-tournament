teams =[{"id":1,"name":"","played":None,"wins":None,"draws":None,"losses":None,"goals_for":None,"goals_against":None,"points":None},{"id":2,"name":"fksjf","played":None,"wins":None,"draws":None,"losses":None,"goals_for":None,"goals_against":None,"points":None}]
team ={"id":None,"name":"","played":None,"wins":None,"draws":None,"losses":None,"goals_for":None,"goals_against":None,"points":None} 
matches = [{"home_team_id": 1, "away_team_id": 2,"home_goals": 3, "away_goals": 1}]


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
        home_goals = validate_input("enter home team goals: ", "positive_num")
        away_goals = validate_input("enter away team goals: ", "positive_num")
        return home_team_id, away_team_id, home_goals, away_goals

def create_match(home_team_id, away_team_id, home_goals, away_goals):
    match = {
        "home_team_id": home_team_id,
        "away_team_id": away_team_id,
        "home_goals": home_goals,
        "away_goals": away_goals}
    return match

def calculate_points(home_goals, away_goals):
    if home_goals > away_goals:
        return 3, 0
    elif home_goals < away_goals:
        return 0, 3
    else:
        return 1, 1

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
                pass  # show standings
            case 5:
                pass  # show leading team
            case 6:
                pass  # show best attacking team
            case 7:
                pass  # show team success rate
            case 8:
                pass  # show teams without goals
            case 9:
                pass  # show tournament summary
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
            if user_input.isdigit() and int(user_input) > 0:
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




main()
print(teams)