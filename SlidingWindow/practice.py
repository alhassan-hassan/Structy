def maxSumSubArray(arr, k):
    maxVal = float("-inf")
    curVal = 0

    for i in range(len(arr)):
        curVal += arr[i]
        
        if i >= k - 1:
            maxVal = max(maxVal, curVal)
            print(maxVal)
            curVal -= arr[i - (k-1)]

    return maxVal



print(maxSumSubArray([3,4,5,6,7,3,2,3,4], 3))