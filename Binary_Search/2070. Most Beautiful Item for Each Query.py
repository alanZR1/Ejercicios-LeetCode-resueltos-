""" 2070. Most Beautiful Item for Each Query

You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

 

Example 1:

Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
Output: [2,4,5,5,6,6]
Explanation:
- For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
- For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
  The maximum beauty among them is 4.
- For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
  The maximum beauty among them is 5.
- For queries[4]=5 and queries[5]=6, all items can be considered.
  Hence, the answer for them is the maximum beauty of all items, i.e., 6.
Example 2:

Input: items = [[1,2],[1,2],[1,3],[1,4]], queries = [1]
Output: [4]
Explanation: 
The price of every item is equal to 1, so we choose the item with the maximum beauty 4. 
Note that multiple items can have the same price and/or beauty.  
Example 3:

Input: items = [[10,1000]], queries = [5]
Output: [0]
Explanation:
No item has a price less than or equal to 5, so no item can be chosen.
Hence, the answer to the query is 0. """

class Solution(object):
  def maximumBeauty(self,items, queries):
    # Ordenar los ítems por precio
    items.sort()
    

    # creamos un array con el numero de items para procesar (beauty)
    max_beauty = [0] * len(items)
    # asignamos al primer valior de beauty el valor de beauty del primer item
    # ya que es el primer precio y por lo tanto el maximo beauty hasta ese momento
    max_beauty[0] = items[0][1]
    
    for i in range(1, len(items)):
      # vamos asignando el maximo beauty de los items que hemos visto hasta ahora
      # al maximo beauty del item actual, ya que el item actual es el que tiene el precio menor
      max_beauty[i] = max(max_beauty[i-1], items[i][1])
    
    # Procesar cada consulta con binary search
    res = []
    for q in queries:
        left, right = 0, len(items) - 1
        # Inicializamos el mejor índice como -1, ya que no hemos encontrado nada
        best_idx = -1
        
        # Hacemos una búsqueda binaria para encontrar el índice del primer elemento cuyo precio es mayor que q
        while left <= right:
            mid = (left + right) // 2
            
            if items[mid][0] <= q:
                best_idx = mid
                left = mid + 1
            else:
                right = mid - 1
        # Si encontramos un índice válido, tomamos el máximo beauty de ese índice
        res.append(max_beauty[best_idx] if best_idx != -1 else 0)
    
    return res
        
        
items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
queries = [1,2,3,4,5,6]
res = Solution()
print (res.maximumBeauty(items, queries))

