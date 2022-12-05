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
        