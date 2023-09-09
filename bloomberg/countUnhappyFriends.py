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
        