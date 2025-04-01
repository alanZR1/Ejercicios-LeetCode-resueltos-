def merge(nums1, m, nums2, n):
    
    i, j, k = m - 1, n - 1, m + n - 1
    
    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:  
            nums1[k] = nums1[i]  # Mover el mayor al final
            i -= 1
        else:
            nums1[k] = nums2[j]  #
            j -= 1
        k -= 1
    return nums1

nums1 = [0]
m = 0
nums2 = [1]
n = 1

print(merge(nums1, m, nums2, n))