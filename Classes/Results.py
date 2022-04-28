from Classes.Result import Result

class Results:
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

     def printResults(self):
        for r in range(1,16):
            percentWon = round(self.won[r] / self.attempts[r] * 100,2)
            averagePegsLeft = round(self.totalPegsLeft[r] / self.attempts[r],0)

            print ("{:<2} {:<4} {:<4} {:<4}".format(r, percentWon, self.won[r], len(self.winningCombinations[r])))
         