def intersection(arr1, arr2):
    set1 = set(arr1)
    return [item for item in arr2 if item in  set1]

print(intersection([4,2,1,6], [3,6,9,2,10]))

""""
    time complexity: O(n + m)
    space --------:  O(min(n, m))
"""