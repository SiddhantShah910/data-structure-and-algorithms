def remove_duplicates(nums):
    count = {}
    k = 0

    for num in nums:
        if num not in count:
            count[num] = 0
        count[num] += 1

        if count[num] <= 2:
            nums[k] = num
            k += 1

    return k

print(remove_duplicates([1,1,1,2,2,3]))
