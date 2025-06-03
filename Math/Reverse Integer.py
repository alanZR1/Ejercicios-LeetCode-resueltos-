class Solution(object):
    
    def reverse(self, x):
        valor = abs(x)
        
        numstr = str(valor)
        
        numstr = numstr[::-1]    
        
        if x < 0:
            numstr = '-' + numstr
            
        resultado = int(numstr)
        
        return resultado if -2**31 <= resultado <= 2**31 - 1 else 0
    
    
solucion = Solution()
print(solucion.reverse(123)) 