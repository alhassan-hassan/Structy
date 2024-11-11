
for i in range(5 , 1, -1):
        print(i)

from sortedcontainers import SortedDict

class Leaderboard:

    def __init__(self):
        # Dictionary to store each player's score
        self.board = {}
        # SortedDict to store scores in descending order with counts of each score
        self.sortedScores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:
        # Check if player already has a score
        if playerId in self.board:
            oldScore = self.board[oldScore]
            count = self.sortedScores.get(-oldScore)
            if count == 1:
                del self.sortedScores[-oldScore]
            else:
                self.sortedScores[-oldScore]-= 1
            
            newScore = score + oldScore
            self.board[playerId] += score
            self.sortedScores[-oldScore] = self.sortedScores.get(-newScore, 0) + 1
        
        else:
            self.board[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1

    def top(self, K: int) -> int:
        count = total = 0
        for score, count in self.sortedScores.items:
            for i in range(count):
                total -= score
                count += 1
                if count == K:
                    return total
        return total

               

    def reset(self, playerId: int) -> None:
        if playerId in self.sortedScores:
            score = self.board[playerId]
            count = self.sortedScores[-score]
            if count == 1:
                del self.sortedScores[-score]
            else:
                self.sortedScores[-score] -= 1

            del self.board[playerId]    

        # Reset player's score in board and sortedScores
        

# # # important module
# # import math

# # def doTheyBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
# #     # area of triangle
# #     def area(x1, y1, x2, y2, x3, y3):
# #         return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

# #     # function isInside to check the point
# #     def isInside(x1, y1, x2, y2, x3, y3, p1, p2):
# #         # Calculate area of triangle ABC
# #         A = area(x1, y1, x2, y2, x3, y3)

# #         # Calculate area of triangle PBC
# #         A1 = area(x2, y2, x3, y3, p1, p2)

# #         # Calculate area of triangle PAC
# #         A2 = area(x1, y1, x3, y3, p1, p2)

# #         # Calculate area of triangle PAB
# #         A3 = area(x2, y2, x1, y1, p1, p2)

# #         # Check if sum of A1, A2, and A3 is same as A
# #         return A == A1 + A2 + A3

# #     def length(x1, y1, x2, y2):
# #         distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
# #         return distance


# #     ab = length(x1, y1, x2, y2)
# #     bc = length(x2, y2, x3, y3)
# #     ac = length(x1, y1, x3, y3)


# #     if not (ab + bc > ac and bc + ac > ab and ab + ac > bc):
# #         return 0
# #     elif isInside(x1, y1, x2, y2, x3, y3, xp, yp,) and isInside(x1, y1, x2, y2, x3, y3, xq, yq,):
# #         return 3
# #     elif isInside(x1, y1, x2, y2, x3, y3, xp, yp,):
# #         return 1
# #     elif isInside(x1, y1, x2, y2, x3, y3, xq, yq,):
# #         return 2
# #     else:
# #         return 4
























# # import sys
# # import collections

# # def solution(A):
# #   size = len(A)
  
# #   if size < 4:
# #     return -1
  
# #   track = collections.defaultdict(int)
  
# #   for i in range(size):
# #     track[A[i]] += 1
    
# #   for key in track.keys():
# #     if track[key] >= 4:
# #       return 0
    
  
# #   remover = set()
  
# #   for key in track.keys():
# #     if track[key] < 2:
# #       remover.add(key)
      
# #   for key in remover:
# #     del(track[key])
    
# #   allKeys = sorted(track.keys())
  
  
# #   if len(allKeys) < 2:
# #     return -1
  
# #   return int(allKeys[len(allKeys) - 1]) - int(allKeys[len(allKeys) - 2])

# # print(solution([911,1,3,1000,1000,2,2,999,1000,911]))

# # import numpy as np

# # # Percentage data for black faculty
# # faculty_percentages = [2.5, 2.5, 2.7, 2.6, 2.5, 2.5, 2.3, 3.1, 2.4, 2.5, 2.5]

# # # Percentage data for black individuals who graduate
# # graduation_percentages = [4.7, 5.1, 4.9, 4.7, 4.7, 4.4, 4.7, 4.7, 4.8, 4.8, 5.0]

# # # Reshape the arrays as 2D arrays
# # faculty_percentages = np.array(faculty_percentages).reshape(-1, 1)
# # graduation_percentages = np.array(graduation_percentages).reshape(-1, 1)

# # # Calculate the correlation coefficient
# # correlation_coefficient = np.corrcoef(faculty_percentages[:, 0], graduation_percentages[:, 0])[0, 1]

# # print("Correlation coefficient:", correlation_coefficient)



# def counterfeit(arr):
#     if len(arr) == 1:
#         return arr[0]

#     hi = len(arr)

#     mid = hi  // 2
#     odd = None

#     if hi % 2 == 1:
#         odd = arr[mid]

#     lower, upper = arr[0 : mid], arr[mid : hi + 1]
#     if sum(lower) == sum(upper):
#         return odd
#     else:
#         return counterfeit(lower) if sum(lower) < sum(upper) else counterfeit(upper)

    
# print(counterfeit([3, 3, 3, 1, 3, 3, 3, 3,3]))


# def sum (a, b):
#     return a + b

# print(sum(2,-10))