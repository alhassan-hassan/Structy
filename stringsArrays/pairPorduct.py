def pairP(nums, target):
    di = {}

    for index, num in enumerate(nums):
        ratio = target / num
        if ratio in di:
            return (di[ratio], index)

        di[num] = index

print(pairP([3, 2, 5, 4, 1], 8))
