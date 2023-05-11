"""This is a implementation of the game 'Run For It'"""

from argparse import ArgumentParser
import matplotlib.pyplot as plt
import random
import sys 
from time import sleep

class Player:
    """Represents a player in the game

    Attributes:
        name(str): The player's name.
        points(int): the total points earned from each player in the game.
        rolls(list): List that consists of the dice rolls made by the player.
        roll_history(list): List of all the rolls the player makes during the 
            game. 
    """
    
    def __init__(self, name):
        """Initializes new player object with name given

        Args:
            name (str): see class documentation.
            
        Side effects:
            Defines attributes 'name', 'points', 'rolls', 'roll_history'.
        """
        self.name = name
        self.points = 0
        self.rolls = []
        self.roll_history = []

    def roll(self): 
        """Rolling a dice 6 times and adding the values to a list.

        Side effect:
            Modifying the value of self.rolls by appending values. 
        
        Primary author:
            Maria Master
        """
        for roll in range(6):
            roll = random.randint(1, 6)
            self.rolls.append(roll)

    def sorting_sequence(self): 
        """Sorts a list of dice roll values and extracts the unique values to 
            return the roll number and the roll value.
            
            Returns:
                unpacked_set_values(list of tuples): the roll number and roll 
                value.
                
            Primary author:
                Maria Master
                
            Technique claimed:
                Sequence unpacking.
        """
        if len(self.rolls) == 6:
            self.sorted_rolls = sorted(self.rolls)
            self.set_rolls = set(self.sorted_rolls)
                
            set_values = len(self.set_rolls)
                
            if set_values <= 6:
                self.unpacked_set_values = []
                for roll_num, roll in enumerate(self.set_rolls):
                    self.unpacked_set_values.append((roll_num+1, roll))
                return self.unpacked_set_values
                    #roll_num+1 because the index starts at 0
                    #returning it so that if another method calls this method
                    #they can access the unpacked_set_values
            else:
                print(f"{self.name} has more than 6 dice rolls.")
                return None
        else:
            print(f"{self.name} has not rolled the dice 6 times yet.")
        
    def turn(self):
        """Implements the rules of the game for each player's turn.
        
        Side effects:
            Writes to stdout
            Modifies self.rolls, self.roll_history, self.points.
        
        Primary author:
            Madison Pease
        
        Technique claimed:
            Set operations on sets.
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
            print(f"Your sequence: {self.get_dice}\n")

            again = input("Test your luck and roll again? (yes or no) ").lower()
            sleep(2)

            print("Roll again!\n") if again == 'yes' else print("Turn over\n")
            
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
                    
                    unpacked_set_values = []
                    self.get_dice = []
                    for roll_num, roll in enumerate(next):
                        unpacked_set_values.append((roll_num+1, roll))

                    for tup in unpacked_set_values:
                        if tup[0] == tup[1]:
                            self.get_dice.append(tup[1])
                    print(f"Your new sequence: {self.get_dice}\n")
                else:
                    self.get_dice = []
        else:
            print("sorry no 1 in roll")
            
        for items in self.get_dice:
            number += 1
        self.points += (number * 5)
                
        self.roll_history.extend(self.rolls)
        print(f"You got a sequence of {number}!")
        print(f"Your current score: {self.points}\n")
        return self.rolls
    
    def __lt__(self, other):
        """Compares the two players based on their total points and gives 
                an update.
        
        Args:
            other (Players): The other Player instance object compared to.
                
        Returns:
            bool: Would return True if player 1 total points is less than 
                player 2.
                
        Primary author:
            Lily Dinh
                
        Technique claimed:
            Magic methods.
        """ 
        if self.points < other.points:
            print(f"{self.name} currently has less points than {other.name}")
        return self.points < other.points
             
    def __str__(self):
        """Returns a string representation of the Player object.

        Returns:
            str: A string that represents the player's name and thier points.
                
        Primary author:
            Lily Dinh
                
        Technique claimed:
            Magic methods.
        """
        return f"{self.name}'s score: {self.points}" 
        
            
    @classmethod       
    def history_score(cls,player_one,player_two): # Beza Ermias
        """Shows a bar graph of the dice rolls that players one and two
        made throughout the game, along with their final results. 
        
        
        Args:
            player_one (Player): The first player
            player_two (Player): The second player 
            
        Primary author:
            Beza Ermias
            
        Technique claimed:
            Visualizing data with pyplot.
            
        """
        fig,(bar1,bar2) = plt.subplots(1,2)
        fig.suptitle(f"{player_one.name} scored {player_one.points} | \
{player_two.name} scored {player_two.points}")
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

 
class Game():
    """Class that plays the game.
    
    Attributes:
        players (list): list of the names of the players
        winner (bool): determines if a player has won the game or not.
        
    Primary author:
        Madison Pease
    """
    def __init__(self):
        """Initalizes the players and status of game.
        
        Side effects:
            Defines attributes 'players' and 'winner'.
        """
        self.players = []
        self.winner = False
    
    def add_player(self,name):
        """Add player object to self.players.
        
        Args:
            name (str): inherts player name from Player class.
            
        Side effects:
            Modifies self.players by appending Player objects to it.
            
        Technique claimed:
            Composition of two custom classes.
        """
        self.players.append(Player(name))
        
    def round(self):
        """Alternates rounds between players.
        
        Side effects:
            Printing the current players turn.
        """
        for i in range(len(self.players)):
            print("============================================================\
=======")
            print("============================================================\
=======")
            print(f"{self.players[i].name} it's your turn\n")
            rolls =self.players[i].turn()
            self.sabotaging_points(rolls,self.players[(i+1)%2])
            sleep(2)
            
    def sabotaging_points(self,rolls,other_player): # Beza Ermias
        """Uses the current rounds's dice results to determine how many sabotage
            points should be subtracted from the opposing player's total score. 
                
        Args:
            rolls(list[int]): A list of intergers representing the dice rolls
                in the current round
            other_player(Player): A instance of the Player class representing 
                the player. 
            
        Primary author:
            Beza Ermias 
        
        Technique claimed:
            Conditional expression.
        """ 
        rollcount = {1:0,2:0,3:0,4:0,5:0,6:0}
        for r in rolls:
            rollcount[r]+=1
        s_points = 0
        for r in rollcount:  
            s_points += r * 2 if rollcount[r] >= 3 else 0  
        if s_points>0:
            print(f"You have sabotaged the other player by rolling "
                  "three of the same! "
                  f"They lose {s_points} points! ;)")
        else:
            print("You cannot sabotage the other player this round :(")
                
        other_player.points -= s_points
        if other_player.points < 0:
            other_player=0            
            
    def check(self):
        """Checks for the winner of the game.
        
        Side effects:
            Prints winner's score and name
            Modifies self.winner to True if game over.
        """
        for player in self.players:
            if player.points >= 100:
                print("========================================================\
===========")
                print(player)
                print(f"{player.name} Won!!\n")
                self.winner = True

def read_scores(filepath):
    """ Reads the textfile in utf-8 that consists of the players name and scores

    Args:
        filepath (str): The path to the trxt file with the names and highest 
            scores

    Returns:
        dict: A dictionary containing players' names as keys and their
        highest socres as values.
        
    Side effects:
        Writes to stdout.
        
    Primary author:
        Lily Dinh
        
    Technique claimed:
        With statement.
    """
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
    
def update_scores(filepath, player, points):
    """ Updates the textfile that consists of the previous player's name & score.
        Writes their highest score.

    Args:
        filepath (str): The path to the highest score file
        player (str): The name of the player
        points (int): The points to update for the player.
        
    Primary author:
        Lily Dinh
    
    Technique Claimed:
        With statements.
    """
    player_scores = read_scores(filepath)
    if player in player_scores:
        player_scores[player] = max(player_scores[player], points)
    else:
        player_scores[player] = points
        
    with open(filepath, 'w', encoding = "utf-8") as f:
        for name, score in player_scores.items():
            f.write(f"{name},{score}\n")
 
def welcome(name1,name2): 
    """Display to users the rules of the game with an example roll
  
    Args:
        name1 (str): the name of the first player 
        name2 (str): the name of the second player
    
    Side effects:
        Prints welcome message with rules to the console. Prints welcome or 
            goodbye message to the console
        
    Primary author:
        Ashley Kharbanda
        
    Technique claimed:
        Use of f-strings.
    """
    print("===================================================================")
    print(f"Welcome {name1} and {name2} to Run For It!!")
    print("The rules of the game are simple! First person to make it to \
100 points wins!\n1)Each round, each player will roll six dice. \
\n2)If you rolled the number one, you will begin your \
sequence, but if you don't, your turn will end. \n3)If you roll a one, you \
have the option to roll your remaining dice to increase your sequence, \
but if you do not roll a number to continue the sequence, you will lose \
all your points for that round.\nSpecial Rule) You have the chance to sabotage \
your oponent's score! If you roll three or more of \
the same number, your oponent will lose whatever number you rolled times 2!")
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
                                                  
def main(player1 = "player1", player2 = "player2"):
    """Runs the game Run For It
  
    Args:
        player1 (str, optional): The first player's name, default to "player1"
        player2 (str, optional): The first player's name, default to "player2"
    
    Side effects:
        Prints player1's and player2's rolls to the console. Prints previous 
            players' scores to the console
        
    Primary author:
        Ashley Kharbanda
        
    Technique claimed:
        Use of Optional Parameters.    
    """
    my_game = Game()
    
    my_game.add_player(player1)
    my_game.add_player(player2)
    
    welcome(player1,player2)
    
    while not my_game.winner:
        my_game.round()
        my_game.check()
        
    
    print("Here are our previous players' scores: ")
    read_scores("players_highest_score.txt")
    print("\nIn the process of changing scores...")
    update_scores("players_highest_score.txt", my_game.players[0].name, 
                  my_game.players[0].points)
    sleep(2)
    update_scores("players_highest_score.txt",my_game.players[1].name, 
                  my_game.players[1].points)
    sleep(2)
    print ("\nNew updated scores:")
    read_scores("players_highest_score.txt")
    print(f"\n{player1}'s and {player2}'s rolls: ")
    my_game.players[0].history_score(my_game.players[0], my_game.players[1])
       
def parse_args(arglist):
    """ Parse command-line arguments.
    
    Expect two mandatory arguments:
        - player1_name: name of the first player (default is "player1")
        - player2_name: name of the second player (default is "player2")
    
    Args:
        arglist (list of str): arguments from the command line.
    
    Returns:
        namespace: the parsed arguments, as a namespace. 
        
    Primary author:
        Maria Master
        
    Technique claimed:
        ArgumentParser class.
    """
    parser = ArgumentParser()
    parser.add_argument("-p1", "--player1_name",default= "player1", 
                        help = "name of player 1")
    parser.add_argument("-p2", "--player2_name",default= "player2", 
                        help = "name of player 2")
    return parser.parse_args(arglist)

if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.player1_name, args.player2_name)
    