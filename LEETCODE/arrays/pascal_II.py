class Solution:
    def getRow(self, rows: int):
        output = []
        if rows < 0:
            return
        if rows == 0:
            return [1]
        
        output.append([1])
        
        for i in range(rows):
            tempt = [0, *output[-1], 0]
            arr = []
            
            for j in range(1, len(tempt)):
                arr.append(tempt[j-1] + tempt[j])
            output.append(arr)
            
        return output[-1]