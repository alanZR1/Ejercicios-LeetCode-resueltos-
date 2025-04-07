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
        diff = [0] * (n + 1)  # Array de diferencias
    
        # 1. Aplicar los cambios en el array de diferencias
        for start, end, direction in shifts:
            if direction == 1:
                diff[start] += 1
                diff[end + 1] -= 1
            else:
                diff[start] -= 1
                diff[end + 1] += 1

        # 2. Obtener la suma acumulativa de desplazamientos
        shift = 0
        shifted_chars = []
        for i in range(n):
            shift += diff[i]  # Aplicamos el desplazamiento acumulado
            new_char = chr(((ord(s[i]) - ord('a') + shift) % 26) + ord('a'))  # Aplicamos el shift
            shifted_chars.append(new_char)

        return "".join(shifted_chars)

s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]

result = Solution()
print (result.shiftingLetters(s, shifts))