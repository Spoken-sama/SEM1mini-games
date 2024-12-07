import sys
from content import *
from utility_functions import *
def math_challenge_factorial():
    n=randint (1,10)
    print('Math Challenge: Calculate the factorial of ',n)
    factorial_answer = int (input ('Your answer:'))
    if factorial_answer == factorial(n):
        print('Correct! You win a key.')
        return(True)
    else:
        print('Wrong! Try again.')
        return(False)
