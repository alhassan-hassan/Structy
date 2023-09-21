class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.cont = defaultdict(int)
        for num in nums2:
            self.cont[num] += 1

    def add(self, index: int, val: int) -> None:
        num = self.nums2[index]
        self.cont[num] -= 1
        if self.cont[num] < 1:
            del self.cont[num]

        self.nums2[index] += val
        self.cont[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        count = 0
        for num in self.nums1:
            complement = tot - num
            count += self.cont[complement]

        return count
        

