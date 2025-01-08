
def factorial(number_factorial : list[int])-> list[int]:
    factorial_cpt=1
    if number_factorial==0:
        return(1)
    else:
        for i in range (number_factorial):
            factorial_cpt=factorial_cpt*(i+1)
        return(factorial_cpt)




def solve_linear_equation():
    a=randint (1,10)
    b=randint (1,10)
    return(a,b,-b/a)



from random import*
def next_player(player):
    return 1 - player


def empty_grid():
    return [[" " for _ in range(3)] for _ in range(3)]


def display_grid(grid, message):
    print(message)
    for row in grid:
        print("| " + " | ".join(row) + " |")
    print("-------------")


def ask_position():
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


def initialize():
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


def turn(player, player_shots_grid, opponent_grid):
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


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def nearest_prime(n):
    while not is_prime(n):
        n += 1
    return n

def has_won(player_shots_grid):
    return sum(row.count("x") for row in player_shots_grid) == 2