import json
import random


def load_riddles(file):
    with open(file, 'r', encoding='utf-8') as f:
        riddles = json.load(f)
    return riddles
def pere_fouras_riddles():
    riddles = load_riddles("PFRiddles.json")
    selected_riddle = random.choice(riddles)
    question = selected_riddle['question']
    answer = selected_riddle['answer'].lower()

    print("\nPère Fouras: Here is your riddle!")
    print(f"Riddle: {question}")
    attempts = 3

    while attempts > 0:
        player_answer = input("Your answer: ").strip().lower()

        if player_answer == answer:
            print("Correct! You have answered the riddle and earned a key!")
            return True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect. You have {attempts} attempt(s) remaining. Try again!")
            else:
                print(f"Out of attempts! The correct answer was: {answer}. Better luck next time!")
                return False
