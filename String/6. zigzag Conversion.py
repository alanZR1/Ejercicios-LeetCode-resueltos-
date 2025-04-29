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
        # primero verificamos si el número de filas es menor o igual a 1
        if numRows <= 1 or numRows >= len(s):
            return s
        # creamos una lista de filas vacías
        filas = [""] * numRows
        # inicializamos la fila actual y la dirección
        filaActual = 0
        direccion = 1 # 1 para abajo -1 para arriba 
        
        for caracter in s:
        # Añadir el carácter a la fila actual
            filas[filaActual] += caracter
            # Cambiar la dirección si estamos en la primera o última fila
            if filaActual == 0:
                direccion = 1
                # si estamos en la primera fila, cambiamos la dirección a abajo
            elif filaActual == numRows - 1:
                direccion = -1
                # si estamos en la última fila, cambiamos la dirección a arriba
            filaActual += direccion   
        # Devolvemos la cadena resultante uniendo todas las filas con el metodo join        
        return "".join(filas)
    
        
s = "PAYPALISHIRING"
numRows = 4

solucion = Solution()
print(solucion.convert(s, numRows))
