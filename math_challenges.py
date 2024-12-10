import time
from content import *
from utility_functions import *
from classes import *

def math_challenge_factorial(cond):
    if cond:
        screen.clear()  # Clear the screen before drawing game elements
        input_box = pygame.Rect(500, 300, 200, 32)
        zoomimg_backgrounds(background, 1, 0, 0)
        pygame.display.update()
        color_inactive = pygame.Color('white')
        color_active = pygame.Color('dodgerblue2')
        color = color_inactive
        active = False
        text = ''
        font = pygame.font.Font(None, 32)
        n = randint(1, 10)
        correct_answer = factorial(n)
        calcul_message = 'Math Challenge: Calculate the factorial of ' + str(n)
        result_message = ''
        win = False
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if input_box.collidepoint(event.pos):
                        active = not active
                    else:
                        active = False
                    color = color_active if active else color_inactive
                elif event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            if text.isdigit() and int(text) == correct_answer:
                                result_message = 'Correct! You win a key.'
                                win = True
                            else:
                                result_message = 'Wrong! Try again.'
                                win = False
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

            screen.clear()
            zoomimg_backgrounds(background, 1, 0, 0)
            txt_surface = font.render(text, True, color)
            width = max(200, txt_surface.get_width() + 10)
            input_box.w = width
            screen.get_display().blit(txt_surface, (input_box.x + 10, input_box.y + 5))
            pygame.draw.rect(screen.get_display(), color, input_box, 2)

            if result_message:
                result_surface = font.render(result_message, True, pygame.Color('white'))
                screen.get_display().blit(result_surface, (input_box.x, input_box.y + 40))

            if calcul_message:
                calcul_surface = font.render(calcul_message, True, pygame.Color('white'))
                screen.get_display().blit(calcul_surface, (input_box.x - 130, input_box.y - 40))
            pygame.display.update()
            screen.update()

            if win:
                time.sleep(1)
                math_challenge_factorial(True)