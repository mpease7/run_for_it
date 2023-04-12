"""This is a implementation of the game 'Run For It'"""

import random

#Maria Master - code written before Player class created
def roll(self): #Maria Master
    #assuming there is an attribute self.rolls = []
    if len(self.rolls) < 6:
        roll = random.randint(1, 6)
        self.rolls.append(roll)
    else:
        #assuming there is an attribute self.name = name (Player's name)
        print(f"{self.name} has already rolled 6 times.")


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

def play(): #Lily Dinh
    "Create player class"

def turn(): 
    """Experimental function that will end a players turn.
    
    """