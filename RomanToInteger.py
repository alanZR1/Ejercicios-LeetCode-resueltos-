class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        valores = {'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        resultado = 0

        for i in range (len(s) - 1): 

            if valores[s[i]] < valores[s[i + 1]]:
                resultado -= valores[s[i]]
            elif valores[s[i]] >= valores[s[i + 1]]:
                resultado += valores[s[i]]

        resultado += valores[s[-1]]
        
        return resultado
        
        
s = "III" 
solucion = Solution()
print(solucion.romanToInt(s))