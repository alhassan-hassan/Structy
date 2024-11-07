import random
class RandomizedSet:
    def __init__(self):
        self.indices = {}
        self.arr = []
        
    def insert(self, val: int) -> bool:
        if val not in self.indices:
            length = len(self.arr)
            self.indices[val] = length
            self.arr.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.indices:
            index, lastelement = self.indices[val], self.arr[-1]
            self.indices[lastelement], self.arr[index] = index, lastelement
            self.arr.pop()
            del self.indices[val]
            return True
        return False

        
    def getRandom(self) -> int:
        return random.choice(self.arr)


# import random
# class RandomizedSet:

#     def __init__(self):
#         self.ind = {}
#         self.cont = []
        
#     def insert(self, val: int) -> bool:
#         if val not in self.ind:
#             self.ind[val] = len(self.cont)
#             self.cont.append(val)
#             return True
#         return False

#     def remove(self, val: int) -> bool:
#         if val in self.ind:
#             cur_ind, last_element = self.ind[val], self.cont[-1]
#             self.cont[cur_ind], self.ind[last_element] = last_element, cur_ind
#             self.cont.pop()
#             del self.ind[val]
#             return True
        
#         return False
        
#     def getRandom(self) -> int:
#         return random.choice(self.cont)
        


# # Your RandomizedSet object will be instantiated and called as such:
# # obj = RandomizedSet()
# # param_1 = obj.insert(val)
# # param_2 = obj.remove(val)
# # param_3 = obj.getRandom()