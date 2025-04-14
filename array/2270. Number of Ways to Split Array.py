""" Medium

You are given a 0-indexed integer array nums of length n.

nums contains a valid split at index i if the following are true:

The sum of the first i + 1 elements is greater than or equal to the sum of the last n - i - 1 elements.
There is at least one element to the right of i. That is, 0 <= i < n - 1.
Return the number of valid splits in nums.

  """
def waysToSplitArray(nums):
        # sumamos el total de la lista
        sumTotal = sum(nums)
        # inicializamos las variables
        sumaIz = 0  
        count = 0 
        # recorremos la lista
        for i in range(len(nums) - 1):
            # sumamos el valor de la izquierda
            sumaIz += nums[i]
            # restamos el valor de la izquierda al total
            sumaD = sumTotal - sumaIz 
                  # verificamos si la suma de la izquierda es mayor o igual a la de la derecha	
            if (sumaIz >= sumaD):
                # si es asi, sumamos uno al contador
                count += 1 
        return count
    
nums = [10,4,-8,7]
print(waysToSplitArray(nums))
