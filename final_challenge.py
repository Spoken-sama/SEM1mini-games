import json
import random

def treasure_room(selected_player):
    # Local variables
    tv_game = {}
    show = {}
    clues = []
    year = ""
    code_word = ""
    attempts = 3
    answer_correct = False
    if selected_player['keys_won'] < 3:
        print("You need at least 3 keys to unlock the treasure room.")
        return False

    try:
        with open('json files/TRClues.json', 'r') as file:
            tv_game = json.load(file)["Fort Boyard"]
    except FileNotFoundError:
        print("Error: 'TRClues.json' file not found.")
        return
    except json.JSONDecodeError:
        print("Error: Failed to decode JSON file.")
        return

    years = list(tv_game.keys())
    if not years:
        print("Error: No data available in the file.")
        return

    year = random.choice(years)
    programs = tv_game.get(year, {})
    if not isinstance(programs, dict) or not programs:
        print(f"Error: No valid programs available for year {year}.")
        return

    show_name = random.choice(list(programs.keys()))
    show = programs.get(show_name, {})

    clues = show.get('Clues', [])
    code_word = show.get('CODE-WORD', "")

    if not isinstance(clues, list) or len(clues) < 3 or not code_word:
        print(f"Error: Insufficient clues or code word is missing for {show_name}.")
        return

    print(f"Welcome to the treasure room! You're solving for {year}, {show_name}.")
    print("Here are your first three clues:")
    for i in range(3):
        print(f"Clue {i + 1}: {clues[i]}")

    attempts = 3
    answer_correct = False

    while attempts > 0:

        player_answer = input("Enter your answer: ").strip()

        if player_answer.lower() == code_word.lower():
            answer_correct = True
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect! You have {attempts} attempts remaining.")

                if 3 - attempts < len(clues) - 3:
                    extra_clue = clues[3 + (3 - attempts)]
                    print(f"Additional clue: {extra_clue}")
            else:
                print(f"Out of attempts! The correct code word was: {code_word}")


    if answer_correct:
        print("Congratulations! You've successfully unlocked the treasure room!")
    else:
        print("Better luck next time! The treasure room remains locked.")
