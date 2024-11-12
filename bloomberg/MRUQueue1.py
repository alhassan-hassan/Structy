from collections import deque

class MRUQueue:
    def __init__(self, n: int):
        # Initialize deque with elements from 1 to n
        self.queue = deque(range(1, n + 1))

    def fetch(self, k: int) -> int:
        # Fetch the k-th element, remove it, and append it to the end
        value = self.queue[k - 1]  # 1-indexed access, so k-1
        del self.queue[k - 1]      # Remove the k-th element
        self.queue.append(value)   # Move it to the end of the deque
        return value