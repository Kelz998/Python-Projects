"""
This program plays the ancient game of Nimm. 
First, I will generate a function for each player and will use
mathematical equations to figure out how many stones are taken 
and how many stones are left in the game. (if the player inputs 
a number other than one or two, it will not be accepted.)
I will then use a seperate function to show who the winner of 
the game is.
"""

import random

def main():
    print("Let's play the game of Nimm.")
    print('----------------------------------')
    total = 20 #this is the total number of stones in the game.
    player = 1
    while total > 0: #while the 20 and so stones are greater than the value of 0,
        print('')
        print('There are '+ str(total) + ' stones left')
        player_choice = int(input('Player ' + str(player) + ' would you like to remove 1 or 2 stones? '))
        if player_choice == 1:
            total -= 1
            #total -= 1 is the same as total = total - 1
        if player_choice == 2:
            total -= 2
        elif player_choice != 1 and player_choice != 2:
        #if the player inputs another int other than 1 or 2, it will print invalid choice
        #and still have the same amount of stones left in game until 1 or 2 stones removed.
            print('Invalid choice! Remove 1 or 2 stones')
        player += 1 #<--- took me the whole week to figure out switching between player 1 and 2. add to player 1(state in line 17) to equal 2. if the player is assigned to a variable less than two, subtract 2 from the player value. 
        if player > 2: 
            player -= 2 

    print('')
    print('Game over. Player', str(player), 'wins!')

# i didn't even have to use this function.
def player_turn(player):
# this changes the player turn between 1 and 2 by using boolean strings.
    if player == 1:
        return 1
    else:
        return 2
    return player

if __name__ == '__main__':
    main()
