class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        stro = {"0" : "0", "1" : "1", "6" : "9", "9" : "6", "8" : "8"} 

        s, f = 0, len(num) - 1
        
        while s <= f:
            if num[s] not in stro or stro[num[s]] != num[f]:
                return False
            s += 1
            f -= 1             
        return True
        # count = []
        # for char in num:
        #     if char in {"0", "1", "8"}:
        #         count.append(char)
        #     elif char == "6" or char == "9":
        #         count.append(char)
        # return len(count) == len(num)
        
#         count = []
        
#         for  char in num:
#             if char not in stro:
#                 return False
#             count.append(stro[char])
        
#         return num[::-1] == "".join(count)
            
        