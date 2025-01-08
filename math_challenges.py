import random
from random import randint
from content import *
from utility_functions import *



def math_challenge_factorial(selected_player):
    n = randint(1, 10)
    correct_answer = factorial(n)
    print(f'Math Challenge: Calculate the factorial of {n}')
    while True:
        player_answer = input('Your answer: ').strip()
        if player_answer.isdigit() and int(player_answer) == correct_answer:
            print('Correct! You win a key.')
            selected_player['keys_won'] += 1
        else:
            print('Wrong! Try again.')




def math_challenge_prime(selected_player):
    n = randint(10, 20)
    correct_answer = nearest_prime(n)
    print("Math Challenge: Find the nearest prime to ", n, ".")
    player_answer = int(input('Your answer: ').strip())
    if player_answer == correct_answer:
        print('Correct! You win a key.')
        selected_player['keys_won'] += 1
        return True
    else:
        print('Wrong! Try again.')
        return False

def math_challenge_equation(selected_player):
    a, b, correct_solution = solve_linear_equation()
    print("Math Challenge: Solve the equation ", a, "x + ", b, " = 0.")
    player_answer = float(input('What is the value of x: ').strip())
    if player_answer == correct_solution:
        print('Correct! You win a key.')
        selected_player['keys_won'] += 1
        return True
    else:
        print('Wrong! Try again.')
        return False


def math_challenge(selected_player): # This function will randomly select a math challenge
    challenges = [math_challenge_prime(selected_player),math_challenge_equation(selected_player),math_challenge_factorial(selected_player)]
    challenge_index = randint(0, 2)
    challenge = challenges[challenge_index]
    print("\nA random challenge has been selected!")
    return challenge()