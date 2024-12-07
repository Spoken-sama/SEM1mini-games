import pygame
import os

base_path = os.path.dirname('content/game_menu.jpg')
base_path2 = os.path.dirname('content/title-menu.png')

# Construct relative paths to the assets
background_path = os.path.join(base_path,'game_menu.jpg')
title_path = os.path.join(base_path2, 'title-menu.png')

background = pygame.image.load(background_path)
title = pygame.image.load(title_path)