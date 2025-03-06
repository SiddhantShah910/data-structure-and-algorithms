def cont_duplicate(nums):
    duplicate = set()
    for num in nums:
        if num in duplicate:
            return True
        duplicate.add(num)
    return False

print(cont_duplicate([1,2,3,4,1]))
