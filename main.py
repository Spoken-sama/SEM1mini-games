running = True
from pere_fouras_challenge import*
from chance_challenges import*
from logical_challenges import*
from final_challenge import*
from math_challenges import*
from game_state import*
def main_menu():
    while True:
        print("\n===== Main Menu =====")
        print("1. Math challenges")
        print("2. Chance Challenges")
        print("3. Logical Challenge")
        print("4. Pere Fouras Challenge")
        print("5. Leave Menu")
        print("==========================")

        choice = input("Enter Your choice : ").strip()
        
        if choice == "1":
            print("\n>>> Starting Math challenges...")
            math_challenge()
        elif choice == "2":
            print("\n>>> Starting Chance Challenges...")
            chance_challenge()
        elif choice == "3":
            print("\n>>> Starting Logical Challenge...")
            battleship_game()
        elif choice == "4":
            print("\n>>> Starting Pere Fouras Challenge...")
            pere_fouras_riddles()
        elif choice == "5":
            print("\nThank you for playing! See you soon!")
            break
        else:
            print("\nImpossible choice! Chose a number between 1 and 5!")

main_menu()
