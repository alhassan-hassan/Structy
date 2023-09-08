import random

class RandomizedCollection:
    def __init__(self):
        self.ind = defaultdict(set)
        self.cont = []
        
    def insert(self, val: int) -> bool:
        self.ind[val].add(len(self.cont))
        self.cont.append(val)
        return len(self.ind[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.ind[val]: return False

        ind, last = self.ind[val].pop(), self.cont[-1]
        self.cont[ind] = last
        self.ind[last].add(ind)
        self.ind[last].discard(len(self.cont) - 1)

        self.cont.pop()

        return True
        
    def getRandom(self) -> int:
        return random.choice(self.cont)
           
"""
Complexity Analysis

Time complexity : O(N)O(N)O(N), with NNN being the number of operations. All of our operations are O(1)O(1)O(1), giving N∗O(1)=O(N)N * O(1) = O(N)N∗O(1)=O(N).

Space complexity : O(N)O(N)O(N), with NNN being the number of operations. The worst case scenario is if we get NNN add operations, in which case our ArrayList and our HashMap grow to size NNN.
"""

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()