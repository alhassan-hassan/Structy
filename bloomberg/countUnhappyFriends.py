class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pref = {}

        # GET EACH PERSON AND THE PERSON(S) THEY PREFERE MORE THAN THE ONE THEY ARE PAIRED WITH
        for x, y in pairs:
            pref[x] = set(preferences[x][0 : preferences[x].index(y)])
            pref[y] = set(preferences[y][0 : preferences[y].index(x)])

        count = 0

        # SOMEONE ISN'T HAPPY IF THEY PREFERE SOMEONE TO THE PERSON THEY ARE PAIRED WITH.
        # AND THAT PERSON ALSO PREFERS THEM TO THE PERSON THEY ARE ALSO PAIRED WITH
        for x in pref:
            for y in pref[x]:
                if x in pref[y]:
                    # if one is found, we move to the next person (break)
                    count += 1
                    break
 
        return count
        

"""
Time Complexity: O(n^2). For each of the n people, we will walk through (up to) n-1 entries in their preferences. Therefore, n * (n-1) approaches O(n^2).

Space Complexity: O(n^2). We will have n entries in the dictionary we create, and each one of those can have (up to) n-1 entries in the set. Therefore, n * (n-1) approaches O(n^2).
"""