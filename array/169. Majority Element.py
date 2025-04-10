""" Easy

Given an array nums of size n, 
return the majority element.

The majority element is the element 
that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element 
always exists in the array. """


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None

        # recorremos el array para cada elemento
        for num in nums:
            # si el contador es cero, asignamos el candidato
            if count == 0:
                candidate = num
            # si el elemento es el candidato,
            # incrementamos el contador 
            # de lo contrario lo decrementamos   
            count += (1 if num == candidate else -1)

        return candidate

solucion = Solution()
nums = [2,2,1,1,1,2,2]
print(solucion.majorityElement(nums)) 