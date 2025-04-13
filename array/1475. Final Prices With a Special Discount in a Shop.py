""" Easy

You are given an integer array prices where prices[i]
is the price of the ith item in a shop.

There is a special discount for items in the shop.
If you buy the ith item, then you will receive a discount
equivalent to prices[j] where j is the minimum index such that 
j > i and prices[j] <= prices[i]. Otherwise,
you will not receive any discount at all.

Return an integer array answer where answer[i] 
is the final price you will pay for the ith item of the shop, 
considering the special discount.

  """
  
class Solution(object):
    def finalPrices(self, prices):
        """
        :type prices: List[int]
        :rtype: List[int]
        """
        # Creamos una lista vacía para almacenar los precios finales
        final_prices = []
        # Recorremos la lista de precios
        for i in range(len(prices)):
            # Inicializamos el precio final como el precio original
            final_price = prices[i]
            # Buscamos el primer precio menor o igual al precio actual
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    final_price -= prices[j]
                    break
            # Agregamos el precio final a la lista
            final_prices.append(final_price)
        return final_prices
        