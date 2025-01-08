import pygame
from interface import *
running = True


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

        elif choice == "4":
            print("\n>>> Starting Pere Fouras Challenge...")

        elif choice == "5":
            print("\nThank you for playing! See you soon!")
            break
        else:
            print("\nImpossible choice! Chose a number between 1 and 5!")


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Goodbye!")
            print(1 + 1)
            print("This code runs after quitting Pygame.")
            n = int(input("Enter a number: "))

            if __name__ == "__main__":
                main_menu()
