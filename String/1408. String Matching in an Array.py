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
        ans = []
        words.sort(key=len)
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i] in words[j]:
                    ans.append(words[i])
                    break
        return ans
    
solucion = Solution()
words = ["mass","as","hero","superhero"]
print(solucion.stringMatching(words))