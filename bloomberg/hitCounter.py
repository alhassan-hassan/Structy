from collections import deque

class HitCounter:
    def __init__(self):
        # Queue to store timestamps of hits
        self.hits = deque()

    def hit(self, timestamp: int) -> None:
        # Record the hit by appending the timestamp to the queue
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        # Remove hits that are outside the 5-minute window
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.popleft()
        
        # The number of hits remaining in the queue is the number of hits in the past 5 minutes
        return len(self.hits)