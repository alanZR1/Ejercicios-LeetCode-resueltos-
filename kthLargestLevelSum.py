from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthLargestLevelSum(root, k):
    if not root:
        return -1
    
    # Lista para almacenar las sumas de los niveles
    level_sums = []
    
    # Cola para el recorrido por niveles (BFS)
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_sum = 0
        
        # Procesar todos los nodos en el nivel actual
        for _ in range(level_size):
            node = queue.popleft()
            level_sum += node.val
            
            # Agregar los hijos a la cola para el siguiente nivel
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        # Agregar la suma del nivel a la lista
        level_sums.append(level_sum)
    
    # Si hay menos de k niveles, devolver -1
    if len(level_sums) < k:
        return -1
    
    # Ordenar las sumas en orden descendente
    level_sums.sort(reverse=True)
    
    # Devolver la k-ésima suma más grande
    return level_sums[k - 1]