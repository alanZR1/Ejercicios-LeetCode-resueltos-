""" Easy

You are given an integer array gifts denoting the number of gifts in various piles. Every second, you do the following:

Choose the pile with the maximum number of gifts.
If there is more than one pile with the maximum number of gifts, choose any.
Reduce the number of gifts in the pile to the floor of the square root of the original number of gifts in the pile.
Return the number of gifts remaining after k seconds.

 

Example 1:

Input: gifts = [25,64,9,4,100], k = 4
Output: 29
Explanation: 
The gifts are taken in the following way:
- In the first second, the last pile is chosen and 10 gifts are left behind.
- Then the second pile is chosen and 8 gifts are left behind.
- After that the first pile is chosen and 5 gifts are left behind.
- Finally, the last pile is chosen again and 3 gifts are left behind.
The final remaining gifts are [5,8,9,4,3], so the total number of gifts remaining is 29.
Example 2:

Input: gifts = [1,1,1,1], k = 4
Output: 4
Explanation: 
In this case, regardless which pile you choose, you have to leave behind 1 gift in each pile. 
That is, you can't take any pile with you. 
So, the total gifts remaining are 4. """

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


print(pickGifts([25,64,9,4,100], 4)) # 29
"""  
Un heap es una estructura de datos especial que permite acceder
rápidamente al elemento mínimo (o máximo en un heap invertido) en tiempo O(1)
y realizar inserciones o eliminaciones en tiempo O(log n).
"""