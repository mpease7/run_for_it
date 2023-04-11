"""This is a implementation of the game 'Run For It'"""

def sorting_sequence(sequence): #Maria Master
    """ An experimental function for this exercise; 
        This function will sort the 6 numbers that the player gets after rolling
        their dices.
        
    Args:
        sequence(list of int): list of numbers corresponding to the 6 rolls.
    """
def welcome(): #Ashley Kharbanda
    """A experimental function for this exercise;
        This function will display to users the rules of the game with an 
        example roll
    """

def play(): #Lily Dinh
    "Create player class"

def turn():
    """Experimental function that will end a players turn.
    """ 
    player_roll = [2,3,5,4,6,3]
    sequence = [1,2,3,4,5,6]
    if 1 not in player_roll:
        count = 0
        check = 3
        prev = 0
        chance = 0

        player_roll.sort()
        for num in player_roll:
            if num == prev:
                count += 1
            else:
                count = 1
            prev = num

            if count >= check:
                chance = 1

        if chance == 1:
            print("Roll again")
        else:
            print("Turn over")
    if sequence in player_roll:
        again = input("Test your luck and roll again?").lower()
        if again == 'yes':
            print("Roll again!")
        if again == 'no':
            print("Turn over!")
    
        
    """ player 1 player 2
    
    """
    
def history_score(): # Beza Ermias
    """
    The player history score
    
    """