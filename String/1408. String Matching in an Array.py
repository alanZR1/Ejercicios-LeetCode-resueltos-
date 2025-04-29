""" Easy

Given an array of string words, return all strings in words
that are a substring of another word.
You can return the answer in any order.

  """
  
class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # creamos una lista vacia para almacenar los resultados
        ans = []
        # ordenamos la lista de palabras por longitud
        words.sort(key=len)
        # iteramos sobre la lista de palabras
        for i in range(len(words)):
            # iteramos sobre las palabras que vienen despues de la palabra actual
            for j in range(i+1, len(words)):
                # si la palabra actual es un substring de la siguiente
                if words[i] in words[j]:
                    # añadimos la palabra actual a la lista de resultados
                    ans.append(words[i])
                    # salimos del bucle interno , ya no es necesario seguir buscando
                    break
        return ans
    
solucion = Solution()
words = ["mass","as","hero","superhero"]
print(solucion.stringMatching(words))