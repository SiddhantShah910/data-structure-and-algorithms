def rotate(nums, k):
    k = k % len(nums)
    l = 0
    r = len(nums) -1
    def loop(l,r):
        while l < r:
            nums[l],nums[r] = nums[r],nums[l]
            l+=1
            r-=1
    loop(0,len(nums)-1)
    loop(0,k-1)
    loop(k, len(nums)-1)
    return nums
    
print(rotate([1,2,3,4,5],2))