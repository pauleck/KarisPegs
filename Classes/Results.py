# Pegs - Program to play the "Peg game" popular in the "Cracker Barrel" chain of resturants
# Karis Eccleston - 3/15/2022

# This class is used to store results of each game so we can display statistics later

class Results:
    # Setup all the arrays and dictionaries we will use to store statistics
    def __init__(self):
        self.results = []
        self.attempts = {}
        self.won = {}
        self.totalPegsLeft = {}
        self.winningCombinations = {}

        # Calculate stats for each starting position
        for r in range(1,17):
            self.attempts[r] = 0
            self.won[r] = 0
            self.totalPegsLeft[r] = 0
            self.winningCombinations[r] = []

    # Add a result to the arrays and dictionaries
    def addResult(self, result):
         self.results.append(result)

         self.attempts[result.startingPosition] = self.attempts[result.startingPosition] + 1
         if (result.won):
            self.won[result.startingPosition] = self.won[result.startingPosition] + 1

            # See if this is a new winning combination
            foundBefore = False
            for w in self.winningCombinations[result.startingPosition]:
                if (w == result.moves):
                    foundBefore = True

            if (foundBefore == False):
                self.winningCombinations[result.startingPosition].append(result.moves)

         self.totalPegsLeft[result.startingPosition] = self.totalPegsLeft[result.startingPosition] + result.pegsLeft