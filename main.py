from data import teams, matches, teams_plasyed
from Features import add_team, show_all_teams, add_much_result,create_match,create_team
from display import display_menu
from validations import validate_input, team_exist_validation,user_choice
from score_calc import update_team_stats,update_score,calculate_points
# calculate_standings, get_leading_team, get_best_attacking_team, get_team_success_rate, get_teams_without_goals, get_tournament_summary, check_championship_potential




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
main()
print(teams)