""" 
Medium

You are given a string s of lowercase English letters and a 2D 
integer array shifts where shifts[i] = [starti, endi, directioni]. 
For every i, shift the characters in s from the index starti to the index endi 
(inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet 
(wrapping around so that 'z' becomes 'a').
Similarly, shifting a character backward means replacing it with the previous 
letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.

  """

class Solution(object):
    def shiftingLetters(self, s, shifts):
        n = len(s)
        diff = [0] * (n + 1)  # Array de diferencias -> diff = [ 0, 0, 0, 0] para n = 3
    
        # 1. Aplicar los cambios en el array de diferencias
        #   Para cada desplazamiento... 
        for start, end, direction in shifts:
            # ...si el desplazamiento es hacia adelante (1), incrementamos el inicio y decrementamos el final + 1
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        # 2. Obtener la suma acumulativa de desplazamientos
        shift = 0
        # creamos una lista para almacenar los caracteres desplazados
        shifted_chars = []
        for i in range(n):
            # sumamos el desplazamiento acumulado
            shift += diff[i]  
            # new char es el nuevo caracter desplazado
            # chr() convierte el valor ASCII en un caracter
            # ord() convierte el caracter en su valor ASCII
            # el nuevo caracter es el resultado de desplazar el caracter actual
            # por el desplazamiento acumulado
            # el %26 es para asegurarnos de que el desplazamiento no exceda el alfabeto
            new_char = chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a')) 
            shifted_chars.append(new_char)

        return "".join(shifted_chars)

s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]

result = Solution()
print (result.shiftingLetters(s, shifts))