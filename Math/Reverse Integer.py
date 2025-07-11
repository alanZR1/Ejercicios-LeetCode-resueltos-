class Solution(object):
    
    def reverse(self, x):
        valor = abs(x)
        # convertimos el valor absoluto a string
        numstr = str(valor)
        # invertimos el string
        numstr = numstr[::-1]    
        # si el numero original es negativo, agregamos el signo negativo al inicio
        if x < 0:
            numstr = '-' + numstr
            
        resultado = int(numstr)
        
        return resultado if -2**31 <= resultado <= 2**31 - 1 else 0
    

    
solucion = Solution()
print(solucion.reverse(123)) 