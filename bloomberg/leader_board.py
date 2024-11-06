import heapq
import collections
class Leaderboard:

    def __init__(self):
        self.board = collections.defaultdict(int)
        
    def addScore(self, playerId: int, score: int) -> None:
        self.board[playerId] += score 
        
    def top(self, K: int) -> int:
        heap = []
        for x in self.board.values():
            heapq.heappush(heap, x)
            
            if len(heap) > K:
                heapq.heappop(heap)
        
        sum_ = 0
        
        for score in heap:
            sum_ += score
            
        return sum_
        
    def reset(self, playerId: int) -> None:
        del self.board[playerId]
        

# from sortedcontainers import SortedDict
class Leaderboard:
    def __init__(self):
        self.board = {}
        self.sortedScores = SortedDict()
        
    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.board:
            self.board[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            oldVal = self.board[playerId]
            val = self.sortedScores.get(-oldVal)

            if val == 1:
                del self.sortedScores[-oldVal]
            else:
                self.sortedScores[-oldVal] = val - 1

            newVal = oldVal + score
            self.board[playerId] = newVal
            self.sortedScores[-newVal] = self.sortedScores.get(-newVal, 0) + 1

    def top(self, K: int) -> int:
        count = total = 0

        for key, val in self.sortedScores.items():
            for i in range(val):
                total += key
                count += 1

                if count == K:
                    break
            if count == K:
                break

        return total * -1

    def reset(self, playerId: int) -> None:
        score = self.board[playerId]
        if self.sortedScores[-score] == 1:
            del self.sortedScores[-score]
        else:
            self.sortedScores[-score] -= 1

        del self.board[playerId]

        


# # Your Leaderboard object will be instantiated and called as such:
# # obj = Leaderboard()
# # obj.addScore(playerId,score)
# # param_2 = obj.top(K)
# # obj.reset(playerId)

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
            # Remove the old score from sortedScores
            oldScore = self.board[playerId]
            count = self.sortedScores.get(-oldScore)
            if count == 1:
                del self.sortedScores[-oldScore]
            else:
                self.sortedScores[-oldScore] -= 1

            # Update player's score
            newScore = oldScore + score
            self.board[playerId] = newScore
            # Add new score to sortedScores
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1
        else:
            # Add new player score
            self.board[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1

    def top(self, K: int) -> int:
        count = total = 0
        # Traverse sortedScores to accumulate the top K scores
        for score, freq in self.sortedScores.items():
            for _ in range(freq):
                total -= score  # `score` is stored as negative, so subtract to add it positively
                count += 1
                if count == K:
                    return total
        return total

    def reset(self, playerId: int) -> None:
        # Reset player's score in board and sortedScores
        if playerId in self.board:
            oldScore = self.board[playerId]
            # Remove old score from sortedScores
            count = self.sortedScores[-oldScore]
            if count == 1:
                del self.sortedScores[-oldScore]
            else:
                self.sortedScores[-oldScore] -= 1
            # Remove player from board
            del self.board[playerId]