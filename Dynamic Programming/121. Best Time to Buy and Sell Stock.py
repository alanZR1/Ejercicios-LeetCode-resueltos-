""" Easy

You are given an array prices where prices[i]
is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day
to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0. """

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # primero verificamos si existen precios
        # esto es opcional
        if not prices:
            return 0
        
        # inicializamos el precio mínimo y el máximo de la ganancia hasta el momento
        min_price = prices[0]
        max_profit = 0
        # recorremos toda la lista 
        for price in prices:
            # si el precio es menor que el mínimo, lo actualizamos
            if price < min_price:
                min_price = price
            # si la diferencia entre el precio y el mínimo es mayor que la ganancia máxima, actualizamos la ganancia máxima
            elif price - min_price > max_profit:
                max_profit = price - min_price
        
        return max_profit
    
Solution = Solution()
prices = [7,1,5,3,6,4]
print(Solution.maxProfit(prices))  # Output: 5