"""This is a implementation of the game 'Run For It'"""

import random

class Players: #Lily Dinh
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
        self.rolls = []

    def roll(self): #Maria Master
        """ Rolling a dice 6 times and adding the values to a list.
        
            Raises:
                ValueError: if a Player tries to roll more than 6 times. 
        """
        if len(self.rolls) < 6:
            roll = random.randint(1, 6)
            self.rolls.append(roll)
        else:
            print(f"{self.name} has already rolled 6 times.")


    def sorting_sequence(self): #Maria Master
        """ An experimental function. Sorts a list of dice roll values and extracts
            the unique values to return the roll number and the roll value.
            
            Returns:
                unpacked_set_values(list of tuples): the roll number and roll value.
        """
        if len(self.rolls) == 6:
            self.sorted_rolls = sorted(self.rolls)
            self.set_rolls = set(self.sorted_rolls)
                
            set_values = len(self.set_rolls)
                
            if set_values <= 6:
                unpacked_set_values = []
                for roll_num, roll in enumerate(self.set_rolls):
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
        
    def turn(self): 
        """Experimental function that will end a players turn.
        """ 
        sequence = {1,2,3,4,5,6} #for testing purposes
        get_dice = []
        
        if 1 not in self.sorted_rolls: #replace w/ sorted frm sorting_sequences method
            count = 0
            check = 3
            prev = 0
            chance = 0

            for num in self.sorted_rolls:
                if num == prev:
                    count += 1
                else:
                    count = 1
                prev = num

                if count >= check:
                    chance = 1

            if chance == 1:
                print("You got 3 of the same! Roll again!")
            else:
                print("You didn't roll a 1! Turn over! :p")
                
        if 1 in self.sorted_rolls:
            combine =  self.set_rolls & sequence
            combined_list = list(combine)
            print(f"You rolled: {combined_list}")

            for tup in unpacked_set_values: #HOW FIX???
                if tup[0] == tup[1]:
                    get_dice.append(tup[1])
            print(f"Your sequence: {get_dice}")

            again = input("Test your luck and roll again? (yes or no)").lower()

            print("Roll again!") if again == 'yes' else print("Turn over")
        
        if again == 'yes': #if player tests luck and rolls again they have to get a number that continues the sequence
            new_roll = []
            rolling = 6 - len(get_dice)
            for i in range(rolling):
                dice = random.randint(1, 6)
                new_roll.append(dice)
                x = sorted(new_roll)
            print(f"You rolled: {x}")
            print("More points!") if get_dice[-1] + 1 in x else print("Turn over! no points")
        

        
            
    def sabotaging_points(perfect_sequence): # Beza Ermias
        """
        If a player gets a perfect sequence this will allow the user subtract two points from the other player
        
        Args:
            perfect_sequence(int): making sure that the person has a perfect sequence which is 6 and less than that
            they will not be able to take the other player point.
        
        
        """        
    def history_score(scores): # Beza Ermias
        """
        The player history score
        
        Args:
            scores(int): the score that will be displayed once the players 
            the game.
        """
        for i in range(len(scores)):
            print(f"Round{i+1}:{scores[1]} points")
            
            
def welcome(self): #Ashley Kharbanda
    """Display to users the rules of the game with an 
            example roll
    """
    print("===================================================================")
    #Since the argument for the send player hasn't been made, I will replace
    #"self.name's friend to their name instead
    print(f"Welcome {self.name} and {self.name}'s friend to Run For It!!")
    print("The rules of the game are simple! First person to make it to \
100 points wins!\n1)Each round, each player will roll six dice. \
\n2)If you rolled the number one, you will begin your \
sequence, but if you don't, your turn will end. \n3)If you roll a one, or 3 \
of the same number, you \
have the option to roll your remaining dice to increase your sequence, \
but if you do not roll a number to continue the sequence, you will lose \
all your points for that round.")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Example: \nRoll: 1,3,4,4,5,6 \nI will choose to roll the \
remaining 5 again because I got a 1 in my sequence \nNew Role: \
1,2,3,3,5,6 \nBecause I have a sequence of 1,2,3 my score will \
translate to 15 points and my turn will be over \nMy friend and \
I will both keep having turns until one of us reach a \
score of 100")
    print("===================================================================")
    while True:
        play_choice = (input("Would you like to keep playing? Type 'Y' or \
    'N'").lower().strip())
        if play_choice[0] not in ["y","n"]:
            print("Invalid choice, please write 'Y' or 'N'")
        elif play_choice == "y":
            print("Have Fun!")
            break #test for now, otherwise prints game board and starts game
        else:
            print("I'm sorry to hear that! Goodbye!")
            break