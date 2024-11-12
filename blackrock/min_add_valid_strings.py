class Solution:
    def addMinimum(self, word: str) -> int:
        exp = "abc"
        ins = 0
        circles = 0

        for char in word:
            while char != exp[circles]:
                ins += 1
                circles = (circles + 1) % 3
            circles = (circles + 1) % 3

        while circles != 0:
            ins += 1
            circles = (circles + 1) % 3

        return ins
            

        # # We define the expected characters in cycle 'abc'
        # expected = 'abc'
        
        # # To track the number of insertions needed
        # insertions = 0
        
        # # We track the current position in the 'abc' cycle
        # cycle_index = 0
        
        # # Iterate through the word
        # for char in word:
        #     # If the current character doesn't match the expected character in the cycle
        #     while char != expected[cycle_index]:
        #         # We need to insert the expected character and move the cycle index forward
        #         insertions += 1
        #         cycle_index = (cycle_index + 1) % 3
            
        #     # If the character matches the expected one, move the cycle index forward
        #     cycle_index = (cycle_index + 1) % 3
        
        # # After the loop, check how many insertions are required for the rest of the cycle
        # while cycle_index != 0:
        #     insertions += 1
        #     cycle_index = (cycle_index + 1) % 3
        
        # return insertions