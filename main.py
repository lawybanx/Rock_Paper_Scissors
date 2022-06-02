from random import choice


def rock_paper_scissors():
    game_choice = ["R", "P", "S"]
    choice_name = {
        "R": "Rock",
        "P": "Paper",
        "S": "Scissors"
    }

    print(f'''
Welcome to the Rock, Paper, Scissors game!!!!
____________________________________________
Instructions:
You have three choices;
Rock(R), Paper(P), Scissors(S)
____________________________________________
    ''')
    player = input('Enter your Choice ("R", "P" or "S"): ').upper()

    is_running = True

    while is_running:
        cpu = choice(game_choice)

        if player not in game_choice:
            print("Invalid choice, Try again")
            player = input('Enter your Choice ("R", "P" or "S"): ').upper()

        elif player == cpu:
            print(f"Player({choice_name[player]}) : CPU ({choice_name[cpu]})")
            print("It's a Tie, Try again")
            player = input('Enter your Choice ("R", "P" or "S"): ').upper()

        elif player == "R" and cpu == "S" or player == "P" and cpu == "R" or player == "S" and cpu == "P":
            print(f"Player({choice_name[player]}) : CPU ({choice_name[cpu]})")
            print(f"Player Wins: {choice_name[player]} beats {choice_name[cpu]}")
            is_running = False

        else:
            print(f"Player({choice_name[player]}) : CPU ({choice_name[cpu]})")
            print(f"Computer Wins: {choice_name[cpu]} beats {choice_name[player]}")
            is_running = False


def play_game():
    play = True
    rock_paper_scissors()
    while play:
        continue_game = input("Do you wish to play again (Y) or (N)? ").upper()
        if continue_game == "N":
            play = False
        elif continue_game == "Y":
            rock_paper_scissors()
        else:
            print("Sorry, I didn't catch that")
            continue


play_game()
