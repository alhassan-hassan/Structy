class Solution:
    def generate(self, rows: int):
        output = []
        if rows < 1:
            return []
        
        output.append([1])
        
        for i in range(rows - 1):
            tempt = [0, *output[-1], 0]
            arr = []
            
            for j in range(1, len(tempt)):
                arr.append(tempt[j-1] + tempt[j])
            output.append(arr)
            
        return output
        