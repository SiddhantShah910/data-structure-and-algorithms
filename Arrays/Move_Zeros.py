def move_zeros(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right] != 0:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
    return nums

print(move_zeros([0,1,0,3,5,7]))
