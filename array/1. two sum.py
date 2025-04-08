""" Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
 """

class Solution:
    def twoSum(self, nums, target):
        # inicializamos un diccionario para ir guardando valores
        # y sus índices para no repetir elementos
        dic = {}  
        # recorremos la lista de números
        # con su indice y su elemento en el array
        for index1, num in enumerate(nums):
            # calculamos el complemento de num actual
            complement = target - num
            # verificamos si el complemento ya existe en el diccionario
            if complement in dic:
                # si existe, retornamos el índice del complemento y el índice actual
                return [dic[complement], index1]
            # si no existe, lo agregamos al diccionario
            dic[num] = index1      # dic {num: index1}
        # si no encontramos la solución, retornamos None    
        return None


nums = [2,7,11,15]
target = 9
solucion = Solution()

print(solucion.twoSum(nums, target))

