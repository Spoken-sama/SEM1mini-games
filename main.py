from pere_fouras_challenge import*
from chance_challenges import*
from logical_challenges import*
from final_challenge import*
from math_challenges import*
from utility_functions import*
import pygame
import os

def main_menu():
    while True:
        print("\n===== Main Menu =====")
        print("1. Math challenges")
        print("2. Chance Challenges")
        print("3. Logical Challenge")
        print("4. Pere Fouras Challenge")
        print("5. Final Challenge")
        print("6. Leave Menu")
        print("==========================")

        choice = input("Enter Your choice : ").strip()

        if choice == "1":
            print("\n>>> Starting Math challenges...")
            selected_player = choose_player(team)
            math_challenge(selected_player)
        elif choice == "2":
            print("\n>>> Starting Chance Challenges...")
            selected_player = choose_player(team)
            chance_challenge(selected_player)
        elif choice == "3":
            print("\n>>> Starting Logical Challenge...")
            selected_player = choose_player(team)
            battleship_game(selected_player)
        elif choice == "4":
            print("\n>>> Starting Pere Fouras Challenge...")
            selected_player = choose_player(team)
            pere_fouras_riddles(selected_player)
        elif choice == "5":
            print("\n>>> Starting Final Challenge...")
            selected_player = choose_player(team)
            treasure_room(selected_player)
        elif choice == "6":
            print("\nThank you for playing! See you soon!")
            break
        else:
            print("\nImpossible choice! Chose a number between 1 and 5!")


pygame.mixer.init()
music_path = os.path.join(os.path.dirname(__file__), "content", "Boyard_music.mp3")


pygame.mixer.music.load(music_path)
pygame.mixer.music.play(-1)



team = compose_equipe()
for player in team:
    print(player)
main_menu()



