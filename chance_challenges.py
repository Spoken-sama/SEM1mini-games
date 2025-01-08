import random
from random import randint



def shell_game(selected_player):
    shells = ['A', 'B', 'C']
    attempts = 0
    max_attempts = 2

    print("Welcome to the Shell Game!")
    print("Guess under which shell (A, B, or C) the key is hidden.")
    print(f"You have {max_attempts} attempts to find the key.")

    while attempts < max_attempts:
        key_shell = random.choice(shells)
        print(f"\nAttempt {attempts + 1} of {max_attempts}:")
        print("Shells: A, B, C")
        player_choice = input("Choose a shell (A, B, or C): ").strip().upper()
        if player_choice in shells:
            if player_choice == key_shell:
                print(f"Congratulations! You found the key under shell {key_shell}.")
                selected_player['keys_won'] += 1
                return True
            else:
                print(f"Sorry, the key was not under shell {player_choice}.")
        else:
            print("Invalid choice! Please choose A, B, or C.")

        attempts += 1

    print(f"\nYou lost! The key was under shell {key_shell}. Better luck next time!")
    return False





def roll_dice_game(selected_player):
    max_attempts = 3
    print("Welcome to the Rolling Dice Game!")
    print("The first to roll a 6 wins. You have up to 3 attempts.")
    for attempt in range(1, max_attempts + 1):
        print(f"\nAttempt {attempt} of {max_attempts}:")
        print("Your turn! Press Enter to roll the dice.")
        input()
        player_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"You rolled: {player_dice[0]} and {player_dice[1]}.")
        if 6 in player_dice:
            print("Congratulations! You rolled a 6 and won the game!")
            selected_player['keys_won'] += 1
            return True
        print("Now it's the game master's turn...")
        master_dice = (random.randint(1, 6), random.randint(1, 6))
        print(f"The game master rolled: {master_dice[0]} and {master_dice[1]}.")
        if 6 in master_dice:
            print("The game master rolled a 6 and wins the game. Better luck next time!")
            return False
        print("No 6 was rolled. Moving on to the next attempt.")
    print("\nIt's a draw! Neither you nor the game master rolled a 6.")
    return False


def chance_challenge(selected_player): #This function will randomly select a challenge
    challenges = [shell_game(selected_player),roll_dice_game(selected_player)]
    challenge_index = randint(0, 1)
    challenge = challenges[challenge_index]
    print("\nA random challenge has been selected!")
    return challenge()