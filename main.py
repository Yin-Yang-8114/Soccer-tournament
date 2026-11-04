from data import teams, matches, teams_plasyed
from Features import *
from display import display_menu
from validations import validate_input, team_exist_validation,user_choice
from score_calc import update_team_stats,update_score,calculate_points




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


if __name__=="__main__":
    main()