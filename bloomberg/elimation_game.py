class Solution:
    def lastRemaining(self, n: int) -> int:
        left_turn = True
        step = 1
        last = 1

        while n != 1:
            if left_turn or n % 2 == 1:
                last += step

            n  = n // 2
            step *= 2
            left_turn = not left_turn

        return last


        # head = 1
        # step = 1
        # left = True
        
        # while n > 1:
        #     # Move head if we're going left or if n is odd when going right
        #     if left or n % 2 == 1:
        #         head += step
            
        #     # Update for the next round
        #     n //= 2
        #     step *= 2
        #     left = not left
        
        # return head