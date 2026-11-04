    if not any(team["name"] == val for team in teams) and not any(team["id"] == val for team in teams):
        print("team does not exist")
        return False
    return True