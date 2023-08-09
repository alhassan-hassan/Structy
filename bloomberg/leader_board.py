import heapq
import collections
class Leaderboard:

    def __init__(self):
        self.board = collections.defaultdict(int)
        self.res = []
        
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
        

from sortedcontainers import SortedDict
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

        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)