""" Medium

Given an integer array nums, rotate the array to the right
by k steps, where k is non-negative.

  """
  
def rotate(nums, k):
    # sacamos el modulo de k para evitar rotaciones innecesarias 
    # si k es mayor que la longitud de nums 
    # por ejemplo si nums tiene 7 elementos y k es 10,
    # rotar 10 veces es lo mismo que rotar 3 veces
    k %= len(nums)
    # invertimos el array completo
    nums.reverse()
    # invertimos los primeros k elementos
    nums[:k] = reversed(nums[:k])
    # invertimos el resto de los elementos
    nums[k:] = reversed(nums[k:])
    return nums

nums = [1, 2, 3, 4, 5, 6, 7]
k = 5

print(rotate(nums, k))