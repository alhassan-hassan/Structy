class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        sl, fs = 0, len(s) - 1
        s = s.lower()
        
        while sl < fs:
            if not s[sl].isalnum():
                sl += 1
            elif not s[fs].isalnum():
                fs -= 1
            elif s[sl] != s[fs]:
                return False
            else:
                sl += 1
                fs -= 1
                
        return True
        