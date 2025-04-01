class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1 or numRows >= len(s):
            return s
        
        filas = [""] * numRows
        filaActual = 0
        direccion = 1 # 1 para abajo -1 para arriba 
        
        for caracter in s:
        # Añadir el carácter a la fila actual
            filas[filaActual] += caracter
            
            if filaActual == 0:
                direccion = 1
            elif filaActual == numRows - 1:
                direccion = -1
            filaActual += direccion   
                
        return "".join(filas)
    
        
s = "PAYPALISHIRING"
numRows = 4

solucion = Solution()
print(solucion.convert(s, numRows))
