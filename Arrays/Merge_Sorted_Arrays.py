def merge_sorted_arrays(nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        nums1.extend([0] * n)
        last = m+n-1
        
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m-=1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last-=1
        while n > 0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last-1
        
        return nums1

print(merge_sorted_arrays([1,3,5],[2,4,6]))