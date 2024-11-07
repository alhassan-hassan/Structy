from typing import List, Dict

class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        pref = {}

        # TRACK ALL UNHAPPY PREFERENCES
        for x, y in pairs:
            pref[x] = set(preferences[x][0 : preferences[x].index(y)])
            pref[y] = set(preferences[y][0 : preferences[y].index(x)])

        unhappyFriends = 0

        for x in pref:
            for y in pref[x]:
                if x in pref[y]:
                    unhappyFriends += 1
                    break
        return unhappyFriends


    #     # Create partner lookup dictionary
    #     partner = {}
    #     for x, y in pairs:
    #         partner[x] = y
    #         partner[y] = x

    #     # Create a ranking dictionary for quick preference comparisons
    #     ranking = {i: {} for i in range(n)}
    #     for i in range(n):
    #         for rank, friend in enumerate(preferences[i]):
    #             ranking[i][friend] = rank

    #     # Count unhappy friends
    #     unhappy_count = 0
    #     for x in range(n):
    #         y = partner[x]
    #         for u in preferences[x]:
    #             # If x prefers u over their current partner y
    #             if ranking[x][u] < ranking[x][y]:
    #                 v = partner[u]
    #                 # And u prefers x over their current partner v
    #                 if ranking[u][x] < ranking[u][v]:
    #                     unhappy_count += 1
    #                     break  # Stop further checks once x is confirmed unhappy

    #     return unhappy_count

    # def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
    #     pref = {}

    #     # GET EACH PERSON AND THE PERSON(S) THEY PREFERE MORE THAN THE ONE THEY ARE PAIRED WITH
    #     for x, y in pairs:
    #         pref[x] = set(preferences[x][0 : preferences[x].index(y)])
    #         pref[y] = set(preferences[y][0 : preferences[y].index(x)])

    #     count = 0

    #     # SOMEONE ISN'T HAPPY IF THEY PREFERE SOMEONE TO THE PERSON THEY ARE PAIRED WITH.
    #     # AND THAT PERSON ALSO PREFERS THEM TO THE PERSON THEY ARE ALSO PAIRED WITH
    #     for x in pref:
    #         for y in pref[x]:
    #             if x in pref[y]:
    #                 # if one is found, we move to the next person (break)
    #                 count += 1
    #                 break
 
    #     return count
        

"""
Time Complexity: O(n^2). For each of the n people, we will walk through (up to) n-1 entries in their preferences. Therefore, n * (n-1) approaches O(n^2).

Space Complexity: O(n^2). We will have n entries in the dictionary we create, and each one of those can have (up to) n-1 entries in the set. Therefore, n * (n-1) approaches O(n^2).
"""