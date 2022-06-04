#total = sum([int(i) for i in lst if type(i)== int or i.isdigit()])
class Solution:
    def digitSum(self, s, k):
        
        if len(s) <= 3:
            return s
        
        tempt = s
        
        while len(tempt) > k:
            grp = len(tempt) // k
            rsd = len(tempt) % k
            
            sec = ""
            
            for i in range(grp):
                sec1 = tempt[i * k : i * k + k]
                sec += str(sum([int(j) for j in sec1]))
                
                if (i + 1) * k == k * grp and rsd > 0:
                    sec += str(sum([int(j) for j in tempt[k * grp  : ]]))
            tempt = sec
            print(tempt)
            
        return tempt
                    
         