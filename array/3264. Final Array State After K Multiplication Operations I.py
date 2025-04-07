""" Easy

You are given an integer array nums, an integer k, and an integer multiplier.

You need to perform k operations on nums. In each operation:

Find the minimum value x in nums. If there are multiple occurrences of the minimum value, select the one that appears first.
Replace the selected minimum value x with x * multiplier.
Return an integer array denoting the final state of nums after performing all k operations.

  """
  
class Solution(object):
    def getFinalState(self, nums, k, multiplier):
        """
        :type nums: List[int]
        :type k: int
        :type multiplier: int
        :rtype: List[int]
        """
        
        for i in range(k):
            min_value = min(nums)
            min_index = nums.index(min_value)
            
            nums[min_index] = min_value * multiplier
        
        return nums
    
solucion = Solution()
nums = [1, 2, 3, 4, 5]
k = 3
multiplier = 2
result = solucion.getFinalState(nums, k, multiplier)
print(result)  # Output: [2, 4, 6, 8, 10]