from logical_challenges import *
from math_challenges import *
from classes import *


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

        while cond:
            screen.clear()
            zoomimg_backgrounds(background, 1, 0, 0)
            zoomimg_backgrounds(title, 0.5, 505, 50)
            Math_chall = Button(screen.get_display(), 480, 300, 300, 70, "Math Challenges", math_challenge, 0,0, 0, 255)
            Chance_chall = Button(screen.get_display(), 480, 380, 300, 70, "Chance Challenges", chance_challenges, 0,0, 0, 255)
            Logical_chall = Button(screen.get_display(), 480, 460, 300, 70, "Logical Challenges", Logical_Challenges, 0, 0, 0, 255)
            Fouras_chall = Button(screen.get_display(), 480, 540, 300, 70, "Pere Fouras Challenges", pere_fouras_challenges, 0,0, 0, 255)
            Final_chall = Button(screen.get_display(), 480, 620, 300, 70, "Final Challenges", final_challenge, 0,0, 0, 255)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if Math_chall.is_clicked(mouse_x, mouse_y):
                        math_challenge(True)
                    elif Chance_chall.is_clicked(mouse_x, mouse_y):
                        chance_challenges(True)
                    elif Logical_chall.is_clicked(mouse_x, mouse_y):
                        Logical_Challenges(True)
                    elif Fouras_chall.is_clicked(mouse_x, mouse_y):
                        pere_fouras_challenges(True)
                    elif Final_chall.is_clicked(mouse_x, mouse_y):
                        final_challenge(True)


            pygame.display.update()
            screen.update()

    else:
        pygame.mixer.music.stop()
        screen.clear()


def Logical_Challenges(cond):
    if cond:
        Menu(False)
        game_1()

def math_challenge(cond):
    if cond:
        Menu(False)
        math_challenge_factorial(True)


def final_challenge(cond):
    if cond:
        pass

def chance_challenges(cond):
    if cond:
        pass

def pere_fouras_challenges(cond):
    if cond:
        pass