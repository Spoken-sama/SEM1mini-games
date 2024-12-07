import interface
from content import *
from utility_functions import *
from classes import *

def math_challenge_factorial(cond):
    if cond:
        screen.clear()  # Clear the screen before drawing game elements
        input_box = pygame.Rect(702, 96, 200, 32)
        zoomimg_backgrounds(background, 1, 0, 0)
        pygame.display.update()
        color_inactive = pygame.Color('white')
        color = color_inactive
        text = ''
        font = pygame.font.Font(None, 32)
        n = randint(1, 10)
        print('Math Challenge: Calculate the factorial of', n)
        factorial_answer = int(input('Your answer:'))
        if factorial_answer == factorial(n):
            print('Correct! You win a key.')
            return True
        else:
            print('Wrong! Try again.')
            return False
