class Solution:
    def twoSum(self, nums, target):
        dic = {}  
        for index1, num in enumerate(nums):
            complement = target - num
            if complement in dic:
                return [dic[complement], index1]
            dic[num] = index1 
        return None


nums = [2,7,11,15]
target = 9
solucion = Solution()

print(solucion.twoSum(nums, target))

