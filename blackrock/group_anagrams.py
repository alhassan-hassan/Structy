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
	•	Time Complexity: O(n \cdot k), where n is the number of strings and k is the average length of the strings.
	•	Space Complexity: O(n \cdot k), dominated by the space required to store the input strings and the dictionary entries.
"""