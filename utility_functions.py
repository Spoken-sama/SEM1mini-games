
def factorial(number_factorial : list[int])-> list[int]: #This function will calculate the factorial of a number
    factorial_cpt=1
    if number_factorial==0:
        return(1)
    else:
        for i in range (number_factorial):
            factorial_cpt=factorial_cpt*(i+1)
        return(factorial_cpt)




def solve_linear_equation(): #This function will solve a linear equation
    a=randint (1,10)
    b=randint (1,10)
    return(a,b,-b/a)



from random import*
def next_player(player): #This function will switch the player
    return 1 - player


def empty_grid(): #This function will create an empty grid
    return [[" " for _ in range(3)] for _ in range(3)]


def display_grid(grid, message): #This function will display the grid
    print(message)
    for row in grid:
        print("| " + " | ".join(row) + " |")
    print("-------------")


def ask_position(): #This function will ask the position
    while True:
        try:
            pos = input("Enter the position (row,column) between 1 and 3 (e.g., 1,2): ")
            row, col = map(int, pos.split(","))
            if 1 <= row <= 3 and 1 <= col <= 3:
                return row - 1, col - 1
            else:
                print("Invalid input. Row and column must be between 1 and 3.")
        except ValueError:
            print("Invalid format. Please enter in the form row,column (e.g., 1,2).")


def initialize(): #This function will initialize the game
    grid = empty_grid()
    for boat_num in range(1, 3):
        print(f"Boat {boat_num}")
        while True:
            row, col = ask_position()
            if grid[row][col] == " ":
                grid[row][col] = "B"
                break
            else:
                print("This position is already occupied. Choose another one.")
    return grid


def turn(player, player_shots_grid, opponent_grid): #This function will switch the turn
    if player == 0:
        display_grid(player_shots_grid, "History of your previous shots:")
        print("It's your turn to shoot!")
        while True:
            row, col = ask_position()
            if player_shots_grid[row][col] == " ":
                break
            print("You already shot at this position. Choose another one.")
    else:
        print("It's the game master's turn:")
        while True:
            row, col = randint(0, 2), randint(0, 2)
            if player_shots_grid[row][col] == " ":
                break
        print(f"The game master shoots at position {row + 1},{col + 1}")

    if opponent_grid[row][col] == "B":
        print("Hit, sunk!")
        player_shots_grid[row][col] = "x"
        opponent_grid[row][col] = "x"
    else:
        print("Splash...")
        player_shots_grid[row][col] = "."


def is_prime(n): #This function will check if a number is prime
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def nearest_prime(n): #This function will find the nearest prime number
    while not is_prime(n):
        n += 1
    return n

def has_won(player_shots_grid): #This function will check if the player has won
    return sum(row.count("x") for row in player_shots_grid) == 2

def solve_linear_equation(): #This function will solve a linear equation
    a = randint(1, 10)
    b = randint(1, 10)
    x = -b / a
    return a, b, x

def compose_equipe(): #This function will compose the team
    MAX_PLAYERS = 3
    team = []

    while True:
        try:
            num_players = int(input("How many players do you wish to include in the team (up to 3)? "))
            if num_players > MAX_PLAYERS:
                print(f"Error: You cannot have more than {MAX_PLAYERS} players.")
                continue
            elif num_players <= 0:
                print("Error: The number of players must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    for i in range(num_players):
        print(f"\nEntering details for player {i + 1}:")
        name = input("Enter player's name: ").strip()
        profession = input("Enter player's profession: ").strip()

        while True:
            is_leader_input = input("Is this player the team leader? (yes/no): ").strip().lower()
            if is_leader_input in ["yes", "no"]:
                is_leader = is_leader_input == "yes"
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

        player = {
            "name": name,
            "profession": profession,
            "is_leader": is_leader,
            "keys_won": 0
        }

        team.append(player)


    if not any(player["is_leader"] for player in team):
        print("\nNo leader was designated. The first player will be assigned as the leader.")
        team[0]["is_leader"] = True

    print("\nTeam composition complete!")
    return team

def choose_player(team): #This function will choose a player
    if not team:
        print("The team is empty. No players to choose from.")
        return None

    print("\nChoose a player to take on the challenge:")
    for i, player in enumerate(team, start=1):
        role = "Leader" if player["is_leader"] else "Member"
        print(f"{i}. {player['name']} ({player['profession']}) - {role}")

    while True:
        try:
            choice = int(input("Enter the player's number: "))
            if 1 <= choice <= len(team):
                selected_player = team[choice - 1]
                print(f"\nYou selected: {selected_player['name']} ({selected_player['profession']}) - {'Leader' if selected_player['is_leader'] else 'Member'}")
                return selected_player
            else:
                print("Invalid number. Please choose a valid player number.")
        except ValueError:
            print("Invalid input. Please enter a number.")