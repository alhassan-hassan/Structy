def smallestSubArray(arr, target):
    #  We should have a window end that takes us to the end of the array.
    # Also, we will need a winsdow start that only increses if we want to shrink the subarray
    
    min_size = float("inf") 
    cur_sum = 0
    start = 0
    
    for end in range(len(arr)):
        cur_sum += arr[end]
        
        while cur_sum >= target:
            min_size = min(min_size, end - start + 1)
            cur_sum -= arr[start]
            start += 1
            
    return min_size 


print(smallestSubArray([4,2,2,7,8,1,2,8,10]), 10)