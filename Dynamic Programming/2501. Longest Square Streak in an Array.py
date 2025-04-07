""" 2501. Longest Square Streak in an Array

Medium

You are given an integer array nums. A subsequence of nums is called a square streak if:

The length of the subsequence is at least 2, and
after sorting the subsequence, each element (except the first element) is the square of the previous number.
Return the length of the longest square streak in nums, or return -1 if there is no square streak.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: nums = [4,3,6,16,8,2]
Output: 3
Explanation: Choose the subsequence [4,16,2]. After sorting it, it becomes [2,4,16].
- 4 = 2 * 2.
- 16 = 4 * 4.
Therefore, [4,16,2] is a square streak.
It can be shown that every subsequence of length 4 is not a square streak.
Example 2:

Input: nums = [2,3,5,6,7]
Output: -1
Explanation: There is no square streak in nums so return -1.
  """
  
import math

class Solution(object):
    def longestSquareStreak(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        dp = {}
        maxim = 1

        for num in nums:
            root = int(math.sqrt(num))
            if root * root == num and root in dp:
                dp[num] = dp[root] + 1
            else:
                dp[num] = 1
            maxim = max(maxim, dp[num])

        return maxim if maxim >= 2 else -1
        
# Ejemplo
nums = [4, 3, 6, 16, 8, 2]  
sol = Solution()
result = sol.longestSquareStreak(nums)
print(result)  