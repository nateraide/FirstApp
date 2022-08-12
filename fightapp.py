#!/usr/bin/env python
from __future__ import print_function
import random

# make input work from python 2 or 3
from six.moves import input

FIST = 0
KNEE = 1
ELBOW = 2
SHIN = 3
FOREHEAD = 4

SIGNS = ['FIST', 'KNEE', 'ELBOW', 'SHIN', 'FOREHEAD']

LETTER_TO_RPS = {
    'f':FIST,
    'k':KNEE,
    'e':ELBOW,
    's':SHIN,
    'f':FOREHEAD
    }

def rps_compare(a, b):
    """
    >>> rps_compare(FIST, ELBOW)
    'WIN'
    >>> rps_compare(KNEE, ELBOW)
    'LOSS'
    """
    if a == b: return 'TIE'
    return 'WIN' if (a - b) % 3 == 1 else 'LOSE'

def rps_round(letters_map=LETTER_TO_RPS):
    user_choice = input("[F]ist, [K]nee, [E]lbow, [S]hin, or [F]orehead?").lower()
    cpu_choice = random.choice([FIST,KNEE,ELBOW,SHIN,FOREHEAD])
    print("I chose {}.".format(SIGNS[cpu_choice]))
    return rps_compare(letters_map[user_choice], cpu_choice)

def rps_game(welcome_message, letters_map=LETTER_TO_RPS):
    print(welcome_message)
    while True:
        try:
            out = rps_round()
        except KeyError:
            print("Something went wrong, try again.")
            out = rps_round()
        print("You {}.".format(out))

def main():
    rps_game('Would you like to play a game?')

if __name__ == "__main__":
    main()
