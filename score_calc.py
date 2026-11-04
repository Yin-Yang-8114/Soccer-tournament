from data import teams, matches, teams_plasyed


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