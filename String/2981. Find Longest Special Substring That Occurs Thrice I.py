"""
MEDIUM 
You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "aaaa"
Output: 2
Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.
Example 2:

Input: s = "abcdef"
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.
Example 3:

Input: s = "abcaba"
Output: 1
Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.
 
 """



class Solution(object):
    def maximumLength(self, s: str) -> int:
        n = len(s)
        # Iterar sobre las longitudes posibles, desde la mayor hasta la menor
        for longitud in range(n, 0, -1):
            conteo = {}
            # Desplazar una ventana de tamaño `longitud` sobre la cadena
            for i in range(n - longitud + 1):
                sub = s[i:i+longitud]
                # Verificar si la subcadena es especial (todos los caracteres son iguales)
                if len(set(sub)) == 1:
                    # Contar las ocurrencias usando un diccionario
                    conteo[sub] = conteo.get(sub, 0) + 1
                    # Si aparece al menos 3 veces, devolver la longitud
                    if conteo[sub] >= 3:
                        return longitud
        return -1  # Si no encontramos ninguna subcadena válida, devolvemos -1


# Crear un objeto de la clase Solution y usarlo
finder = Solution()

# imprimir aplicando metodos 'def'
print(finder.maximumLength("aaaa"))   # Salida: 2
print(finder.maximumLength("abcdef")) # Salida: -1
print(finder.maximumLength("abcaba")) # Salida: 1
