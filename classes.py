import pygame
from content import *

class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("MNI games")
        pygame.display.set_icon(title)
        self.clock = pygame.time.Clock()
        self.framerate = 15

    def update(self):
        pygame.display.flip()
        self.clock.tick(self.framerate)

    def clear(self):
        self.display.fill((0, 0, 0))

    def get_size(self):
        return self.display.get_size()

    def get_display(self):
        return self.display

screen = Screen()




class Button:
    def __init__(self, screen, x, y, length, height, text, function, r, g, b, alpha=255):
        self.screen = screen
        self.length = length
        self.height = height
        self.text = text
        self.rect = pygame.Rect(x, y, length, height)
        self.function = function
        self.color = (r, g, b)
        self.surface = pygame.Surface((length, height), pygame.SRCALPHA)
        self.surface.set_alpha(alpha)

        font = pygame.font.Font(None, 36)
        text_act = font.render(self.text, True, (self.color[0], self.color[1], self.color[2], alpha))
        text_rect = text_act.get_rect(center=(self.surface.get_width() / 2, self.surface.get_height() / 2))
        self.surface.blit(text_act, text_rect)

        # Draw the button on the screen
        self.screen.blit(self.surface, (x, y))

    def is_clicked(self, mouse_x, mouse_y):
        return self.rect.collidepoint(mouse_x, mouse_y)

def zoomimg_backgrounds(image, scale, x, y):
    zoomimg = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
    screen.display.blit(zoomimg, (x, y))
