"""
2INDEX
        integers, check if there exist two indices i and j such that :

        i != j
        h
        arr[i] == 2 * arr[j]
"""
def checkIfExist(arr):

    
    for i in range (len(arr)):
      for j in range (1, len(arr)):
        if (i != j and arr[i] == 2 * [j]):
            return True
    return False

arr = [0, 0]
#print(checkIfExist(arr))


""" CHECK IT BITWISE OR HAS TRAILIING ZEROS """
def hasTrailingZeros(nums):

  for i in range(len(nums)):
      for j in range(len(nums)):
        if i != j:
          if (nums[i] + nums[j]) % 2 == 0:
            return True 
  return False

nums = [1 ,2 ,3 ,4 ,5 ]
#print(hasTrailingZeros(nums))

""" GIFTS """
import heapq
import math


def pickGifts( gifts, k):
    
    gifts = [-x for x in gifts]  # al convertirlos en negativos el mayor se convierte en el menor 
    heapq.heapify(gifts) #convierte una lista en un heap
    while k > 0:
        maxGift = heapq.heappop(gifts) #obtiene el elemento mas pequeño
        raiz = math.sqrt(- maxGift)
        heapq.heappush(gifts, - int(raiz)) # inserta el elemento de forma negativa para ajustar a los demas valores
        k -= 1
    return(-sum(gifts)) # la suma tambien es negativa porque los valores de gifts son negativos

    """  
    Un heap es una estructura de datos especial que permite acceder
    rápidamente al elemento mínimo (o máximo en un heap invertido) en tiempo O(1)
    y realizar inserciones o eliminaciones en tiempo O(log n).
    """
        
""" MARKEST THE SMALLEST ELEMENT """
def findScore(nums):

        n = len(nums)
        marked = [False] * n  
        score = 0

        indexed_nums = sorted((value, idx) for idx, value in enumerate(nums))

        for value, idx in indexed_nums:
            if not marked[idx]: 
                score += value
                marked[idx] = True 
                if idx > 0:  
                    marked[idx - 1] = True
                if idx < n - 1:
                    marked[idx + 1] = True

        return score

""" MINIMUN DELETIONS """

def minimumDeletions(s):
    count_b = 0
    deletions = 0

    for char in s:
        if char == 'b':
            count_b += 1
        else:
            deletions = min(deletions + 1, count_b) 
    return deletions

s = "aababbab"
#print(minimumDeletions(s))

""" NUMBER OF TEAMS """

def numTeams(rating):
    n = len(rating)
    count = 0

    # Para cada soldado en la posición "j", encontrar cuántos soldados antes de él son menores/mayores
    # y cuántos soldados después de él son mayores/menores para formar equipos válidos.
    for j in range(n):
        less_left = less_right = greater_left = greater_right = 0

        # Comparar con los soldados a la izquierda de "j"
        for i in range(j):
            if rating[i] < rating[j]:
                less_left += 1
            elif rating[i] > rating[j]:
                greater_left += 1

        # Comparar con los soldados a la derecha de "j"
        for k in range(j + 1, n):
            if rating[j] < rating[k]:
                less_right += 1
            elif rating[j] > rating[k]:
                greater_right += 1

        # Contar equipos válidos
        count += less_left * less_right + greater_left * greater_right

    return count

rating =   [2,5,3,4,1]
#print(numTeams(rating))


""" PREFIX """

def isPrefixOfWord(sentence, searchWord):
    words = sentence.split()

    for index, word in enumerate(words):
   
        if word.startswith(searchWord): #verifica si inicia con la palabra (argumento)
            return index + 1
    return -1

sentence = "hello from the other side"
searchWord = "they"
#print (isPrefixOfWord(sentence, searchWorld ))

""" RESTORED MATRIX """

def restoreMatrix(rowSum, colSum):
    m, n = len(rowSum), len(colSum)
    matriz = [[0] * n for j in range(m)]
    
    for i in range(m):
        for j in range(n):
            val = min(rowSum[i], colSum[j])
            matriz[i][j] = val
            
            rowSum[i] -= val
            colSum[j] -= val
    return matriz


rowSum = [3,8]
colSum = [4,7]
#print(restoreMatrix(rowSum, colSum))

""" SORTED PEOPLE """
def sortPeople(names, heights):
    people = list(zip(names, heights))
    people.sort(key = lambda x: x[1], reverse = True)
    sorted_names = []
    for person in people:
        sorted_names.append(person[0])
    return sorted_names
    
names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]
#print(sortPeople(names, heights))

