""" Easy

Given an integer x, return true if x is a palindrome, and false otherwise. """

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # convertimos el entero a string
        # y lo convertimos a una lista de digitos
        xlist = [digit for digit in str(x)]
        # definimos los indices de la lista
        # right es el primer elemento 
        right = 0
        # y left el ultimo
        left = len(xlist) - 1
        # mientras right sea menor que left
        while right < left:
            # si el elemento de la derecha no es igual al de la izquierda
            if xlist[right] != xlist[left]:
                # retornamos false
                return False
            # si son iguales, incrementamos right y decrementamos left
            left -= 1
            right += 1
        return True