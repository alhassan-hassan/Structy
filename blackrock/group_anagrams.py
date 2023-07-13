# Approach: Categorize by Count
class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()

"""
Time Complexity: O(NK)O(NK)O(NK), where NNN is the length of strs, and KKK is the maximum length of a string in         strs.           Counting each string is linear in the size of the string, and we count every string.  

Space Complexity: O(NK)O(NK)O(NK), the total information content stored in ans.
"""