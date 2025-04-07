""" Medium

Given an integer array nums, rotate the array to the right
by k steps, where k is non-negative.

  """
  
def rotate(nums, k):
    k %= len(nums)
    
    nums.reverse()
    nums[:k] = reversed(nums[:k])
    nums[k:] = reversed(nums[k:])
    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
k = 5

print(rotate(nums, k))