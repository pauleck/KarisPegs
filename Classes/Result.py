# Pegs - Program to play the "Peg game" popular in the "Cracker Barrel" chain of resturants
# Karis Eccleston - 3/15/2022

# Class to store a result from each game
class Result:
     def __init__(self):
         self.startingPosition = 0;
         self.pegsLeft = 0;
         self.moves = ""
         self.won = False
         