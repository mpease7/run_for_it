"""This is a implementation of the game 'Run For It'"""

import random

class Players:
    """Represents a player in the game

    Attributes:
        name(str): The player's name
        points(int): the total points earned from each player in the game
        rolls(list): List that consists of the dice rolls made by the player 
    """
    
    def __init__(self, name):
        """ Initializes new player object with name given

        Args:
            name (str): The player's name
        """
        self.name = name
        self.points = 0
        self.roll = []

#Maria Master - code written before Player class created
def roll(self): #Maria Master
    """ Rolling a dice 6 times and adding the values to a list.
    
        Raises:
            ValueError: if a Player tries to roll more than 6 times. 
    """
    #assuming there is an attribute self.rolls = []
    if len(self.rolls) < 6:
        roll = random.randint(1, 6)
        self.rolls.append(roll)
    else:
        #assuming there is an attribute self.name = name (Player's name)
        raise ValueError(f"{self.name} has already rolled 6 times.")


def sorting_sequence(self): #Maria Master
    """ An experimental function. Sorts a list of dice roll values and extracts
        the unique values to return the roll number and the roll value.
        
        Returns:
            unpacked_set_values(list of tuples): the roll number and roll value.
    """
    if len(self.rolls) == 6:
        sorted_rolls = sorted(self.rolls)
        set_rolls = set(sorted_rolls)
            
        set_values = len(set_rolls)
            
        if set_values <= 6:
            unpacked_set_values = []
            for roll_num, roll in enumerate(set_rolls):
                unpacked_set_values.append((roll_num+1, roll))
            return unpacked_set_values
                #roll_num+1 because the index starts at 0
                #returning it so that if another method calls this method
                #they can access the unpacked_set_values
        else:
            print(f"{self.name} has more than 6 dice rolls.")
            return None
    else:
        print(f"{self.name} has not rolled the dice 6 times yet.")
        
        
def welcome(): #Ashley Kharbanda
    """A experimental function for this exercise;
        This function will display to users the rules of the game with an 
        example roll
    """



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