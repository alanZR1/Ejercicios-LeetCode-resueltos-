import math 
class Solution(object):
    def pickGifts(self, gifts, k):
        
        for i in range (k):
            pila_maxima = max(gifts)
            indice = gifts.index(pila_maxima)
            raiz = int(math.sqrt(pila_maxima))
            gifts[indice] = raiz
        return int (sum(gifts))

gifts = [25,64,9,4,100]
k = 4
resultado = Solution() 
print (resultado.pickGifts(gifts, k))