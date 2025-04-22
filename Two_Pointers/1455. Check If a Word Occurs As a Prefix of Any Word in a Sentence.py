""" 1455. Check If a Word Occurs As a Prefix of Any Word in a Sentence

Easy

Given a sentence that consists of some words separated by a single space, and a searchWord,
check if searchWord is a prefix of any word in sentence.

Return the index of the word in sentence (1-indexed) where searchWord is a prefix of this word.
If searchWord is a prefix of more than one word, return the index of the first word (minimum index).
If there is no such word return -1.

A prefix of a string s is any leading contiguous substring of s.

 

Example 1:

Input: sentence = "i love eating burger", searchWord = "burg"
Output: 4
Explanation: "burg" is prefix of "burger" which is the 4th word in the sentence.
Example 2:

Input: sentence = "this problem is an easy problem", searchWord = "pro"
Output: 2
Explanation: "pro" is prefix of "problem" which is the 2nd and the 6th word in the sentence,
but we return 2 as it's the minimal index.
Example 3:

Input: sentence = "i am tired", searchWord = "you"
Output: -1
Explanation: "you" is not a prefix of any word in the sentence.
  """
  
def isPrefixOfWord(sentence, searchWord):
    # dividimos la oracion en palabras con el 
    # metodo split() y guardamos en una lista
    words = sentence.split()
     
    # inciamos un ciclo for para recorrer la lista de palabras
    # y el metodo enumerate() para obtener el indice
    for index, word in enumerate(words):
   
        if word.startswith(searchWord): #verifica si inicia con la palabra (argumento)
            # si es verdadero, retorna el indice + 1 
            return index + 1
    return -1

sentence = "hello from the other side"
searchWord = "they"
print (isPrefixOfWord(sentence, searchWord ))