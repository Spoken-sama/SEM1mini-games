import sys
from content import *
from utility_functions import *




def game_1 (cond):
    print("Each player must place 2 boats on a 3x3 grid.")
    print("Boats are represented by 'B' and missed shots by '.'. Sunk boats are marked by 'x'.")

    print("Place your boats:")
    player_grid = initialize()
    display_grid(player_grid, "Here is your game grid with your boats:")

    game_master_grid = empty_grid()
    placed_boats = 0
    while placed_boats < 2:
        row, col = randint(0, 2), randint(0, 2)
        if game_master_grid[row][col] == " ":
            game_master_grid[row][col] = "B"
            placed_boats += 1

    player_shots_grid = empty_grid()
    game_master_shots_grid = empty_grid()

    current_player = 0
    while True:
        if current_player == 0:
            turn(current_player, player_shots_grid, game_master_grid)
            if sum(row.count("x") for row in player_shots_grid) == 2:
                print("The player won!")
                break
        else:
            turn(current_player, game_master_shots_grid, player_grid)
            if sum(row.count("x") for row in game_master_shots_grid) == 2:
                print("The game master won!")
                break
        current_player = next_player(current_player)