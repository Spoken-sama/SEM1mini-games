import interface
from content import *
from utility_functions import *
from classes import *



def game_1 ():
    screen.clear()
    input_box = pygame.Rect(702, 96, 200, 32)
    zoomimg_backgrounds(background, 1, 0, 0)
    pygame.display.update()
    color_inactive = pygame.Color('black')
    color = color_inactive
    text = ''
    font = pygame.font.Font(None, 32)
    print("Each player must place 2 boats on a 3x3 grid.")
    print("Boats are represented by 'B' and missed shots by '.'. Sunk boats are marked by 'x'.")

    print("Place your boats:")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if input_box.collidepoint(event.pos):
                active = not active
            else:
                active = False
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
        txt_surface = font.render(text, True, color)
        input_box.w = max(200, txt_surface.get_width() + 10)
        screen.get_display().blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen.get_display(), color, input_box, 2)

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