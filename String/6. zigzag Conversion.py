""" Medium

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

str 
ing convert(string s, int numRows);
 """
 
 
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
