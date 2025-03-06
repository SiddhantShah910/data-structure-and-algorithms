def max_sub(nums):
    cur_sum = 0
    max_sum = float('-inf')
    
    for i in range(len(nums)):
        cur_sum += nums[i]
        max_sum = max(max_sum, cur_sum)
        
        if cur_sum < 0:
            cur_sum = 0
        
    return max_sum

print(max_sub([5,4,-1,7,8]))
