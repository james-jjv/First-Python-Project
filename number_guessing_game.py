'''
A module containing a function to play a number guessing game using a player
'''

import random

def play(player):
    '''
    plays one round of a number guessing game based on a type of player strategy

    Parameters
    ----------
    player : object instance
        represents a player using a certain strategy to guess numbers

    Returns
    -------
    None.

    '''
    n = random.randint(1, 100)  # choose a random number between 1 and 100 as the correct answer to guess
    while True:
        guess = player.guess()  # player makes a guess
        if guess < n:
            player.outcome('too low')  # incorrect, another guess is made
        elif guess > n:
            player.outcome('too high')  # incorrect, another guess is made
        else:
            player.outcome('correct')  # correct, the round is over
            break