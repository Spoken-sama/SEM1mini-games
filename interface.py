import sys
from logical_challenges import *
from content import *
from utility_functions import *
from math_challenges import *


class Screen:
    def __init__(self):
        self.display = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("C'est ment tix")
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


def buttons(bt1: Button, arg1):
    while True:
        screen.clear()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if bt1.is_clicked(mouse_x, mouse_y):
                    bt1.function(arg1)

        bt1.screen.blit(bt1.surface, bt1.rect.topleft)  # Redraw the button each frame
        pygame.display.update()
        screen.update()

def zoomimg_backgrounds(image, scale, x, y):
    zoomimg = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
    screen.display.blit(zoomimg, (x, y))

def Menu(cond):
    if cond:
        running = True

        while running:
            screen.clear()
            zoomimg_backgrounds(background, 1, 0, 0)
            zoomimg_backgrounds(title, 0.5, 505, 50)
            cemantix = Button(screen.get_display(), 525, 300, 210, 70, "Logical Challenges", Logical_Challenges, 0, 0, 0, 255)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if cemantix.is_clicked(mouse_x, mouse_y):
                        Logical_Challenges(True)

            pygame.display.update()
            screen.update()

    else:
        pygame.mixer.music.stop()






def Logical_Challenges(cond):
    if cond:
        game_1(True)

