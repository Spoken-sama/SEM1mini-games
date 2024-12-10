import pygame
import classes
from interface import *
pygame.init()
running = True
Menu(True)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()






