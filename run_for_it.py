"""This is a implementation of the game 'Run For It'"""

from argparse import ArgumentParser
import random
import matplotlib.pyplot as plt
import sys 
from time import sleep

class Player: #Lily Dinh
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
        self.roll_history = []

    def roll(self): #Maria Master
        """ Rolling a dice 6 times and adding the values to a list.
        
            Raises:
                ValueError: if a Player tries to roll more than 6 times. 
        """
        for roll in range(6):
            roll = random.randint(1, 6)
            self.rolls.append(roll)

    def sorting_sequence(self): #Maria Master -- list.sort() credit claim
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
        
    def turn(self): # Madison Pease - set operations
        """Allows the player to take a turn and how a sequence forms 
        """ 
        self.rolls = []
        self.roll()
        self.sorting_sequence()
        self.get_dice = []
        number = 0
        
        print(f"You rolled: {self.rolls}")
         
        if 1 in self.sorted_rolls:

            for tup in self.unpacked_set_values: 
                if tup[0] == tup[1]:
                    self.get_dice.append(tup[1])
            print(f"Your sequence: {self.get_dice}")

            again = input("Test your luck and roll again? (yes or no) ").lower()
            sleep(2)

            print("Roll again!") if again == 'yes' else print("Turn over")
            
            if again == 'yes':
                new_roll = []
                rolling = 6 - len(self.get_dice)
                for i in range(rolling):
                    dice = random.randint(1, 6)
                    new_roll.append(dice)
                new_set = set(sorted(new_roll))
                print(f"You rolled: {new_roll}")
                
                if self.get_dice[-1] + 1 in new_set:
                    next = new_set | set(self.get_dice)
                    print(next)
                    
                    unpacked_set_values = []
                    self.get_dice = []
                    for roll_num, roll in enumerate(next):
                        unpacked_set_values.append((roll_num+1, roll))

                    for tup in unpacked_set_values:
                        if tup[0] == tup[1]:
                            self.get_dice.append(tup[1])
                    print(f"Your new sequence: {self.get_dice}")
                else:
                    self.get_dice = []
        else:
            print("sorry no 1 in roll")
            
        for items in self.get_dice:
            number += 1
        self.points += (number * 5)
                
        self.roll_history.extend(self.rolls)
        print(f"You got a sequence of {number}! Your current score: {self.points}")
 
        
            
    def sabotaging_points(perfect_sequence): # Beza Ermias
        """
        If a player gets a perfect sequence this will allow the user subtract two points from the other player
        
        Args:
            perfect_sequence(int): making sure that the person has a perfect sequence which is 6 and less than that
            they will not be able to take the other player point.
        
        
        """ 
    @classmethod       
    def history_score(cls,player_one,player_two): # Beza Ermias
        """
        Shows a bar graph of the dice rolls that players one and two
        made throughout the game, along with their final results. 
        
        
        Args:
            player_one (Player): The first player
            player_two (Player): The second player 
            
            
        """
        fig,(bar1,bar2) = plt.subplots(1,2)
        fig.suptitle(f"{player_one.name} scored {player_one.points} | {player_two.name} scored {player_two.points}")
        rolled_charts = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        for roll in player_one.roll_history:
            rolled_charts[roll] = rolled_charts[roll]+1
        print(rolled_charts)
        bar1.bar(rolled_charts.keys(),rolled_charts.values())
        bar1.set_xlabel("Dice Rolls")
        bar1.set_ylabel("Count")
        bar1.set_title(f"Dice Roll By {player_one.name}")

        
        rolled_charts = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
        for roll in player_two.roll_history:
            rolled_charts[roll] = rolled_charts[roll]+1
        print(rolled_charts)
        bar2.bar(rolled_charts.keys(),rolled_charts.values())
        bar2.set_xlabel("Dice Rolls")
        bar2.set_ylabel("Count")
        bar2.set_title(f"Dice Roll By {player_two.name}")
        plt.show()
        
        def __lt__(self, other):
            """ Compares the two players based on their total points and gives an update.
        
            Args:
                other (Players): The other Player instance object compared to.
            Returns:
                bool: Would retirn True if player 1 total points is less than player 2.
            """
            
            if self.points < other.points:
                print(f"{self.name} currently has less points than {other.name}")
            return self.points < other.points 
        
        def __str__(self):
            return f"{self.name}: {self.points} points"
 
class Game():
    def __init__(self):
        self.players = []
        self.winner = False
    
    def add_player(self,name):
        self.players.append(Player(name))
        
    def round(self):
        for player in self.players:
            print("===================================================================")
            print("===================================================================")
            print(f"{player.name} it's your turn")
            player.turn()
            sleep(2)
            
    def check(self):
        for player in self.players:
            if player.points >= 100:
                print("===================================================================")
                print(f"{player.name}'s score: {player.points}")
                print(f"{player.name} Won!!")
                self.winner = True

def read_scores(filepath):
    with open(filepath, 'r', encoding = "utf-8") as f:
        
        player_scores = {}
        for line in f:
            name, score = line.split(",")
            score = int(score.strip())
            
            if name not in player_scores:
                player_scores[name] = score
            else:
                player_scores[name] = max(player_scores[name], score)
        print(player_scores)
        return player_scores
 
def welcome(name1,name2): #Ashley Kharbanda, f-strings
    """Display to users the rules of the game with an example roll
    
    Args:
        name1 (str): the name of the first player 
        name2 (str): the name of the second player
    """
    print("===================================================================")
    print(f"Welcome {name1} and {name2} to Run For It!!")
    print("The rules of the game are simple! First person to make it to \
100 points wins!\n1)Each round, each player will roll six dice. \
\n2)If you rolled the number one, you will begin your \
sequence, but if you don't, your turn will end. \n3)If you roll a one, you \
have the option to roll your remaining dice to increase your sequence, \
but if you do not roll a number to continue the sequence, you will lose \
all your points for that round.")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("Example: \nRoll: 1,3,4,4,5,6 \nI will choose to roll the \
remaining 5 again because I got a 1 in my sequence \nNew Role: \
1,2,3,3,6 \nBecause I have a sequence of 1,2,3 my score will \
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
            break 
        else:
            print("I'm sorry to hear that! Goodbye!")
            exit()
                                                  
def main(player1 = "player1", player2 = "player2"): #Ashley Kharbanda
    #Optional Parameters
    """Runs the game Run For It
    
    Args:
        player1 (str, optional): The first player's name, default to "player1"
        player2 (str, optional): The first player's name, default to "player2"
        
    """
    my_game = Game()
    
    my_game.add_player(player1)
    my_game.add_player(player2)
    
    welcome(player1,player2)
    
    while not my_game.winner:
        my_game.round()
        my_game.check()
    
    print("Here are our previous players' scores: ")
    read_scores("players_highest_scores.txt")
    print(f"\n{player1}'s and {player2}'s rolls: ")
    my_game.players[0].history_score(my_game.players[0], my_game.players[1])
       
def parse_args(arglist): #Maria Master -- ArgumentParser class credit claim 
    """ Parse command-line arguments.
    
    Expect two mandatory arguments:
        - player1_name: name of the first player
        - player2_name: name of the second player
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace. 
    """
    parser = ArgumentParser()
    parser.add_argument("player1_name", help = "name of player 1")
    parser.add_argument("player2_name", help = "name of player 2")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.player1_name, args.player2_name)
    