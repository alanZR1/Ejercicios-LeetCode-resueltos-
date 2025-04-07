# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        l1new = "".join(map(str, l1[::-1]))  # Convierte cada número a string y revierte
        l2new = "".join(map(str, l2[::-1]))
        num1 = int(l1new)
        num2 = int(l2new)
        suma = num1 + num2
        strSuma = str(suma)
        reSuma = strSuma[::-1]
        intSuma = int(reSuma)
        lista = list(map(int, str(intSuma)))
        return lista
    
solution = Solution()

l1 = [2,4,3]
l2 = [5,6,4]

print(solution.addTwoNumbers(l1, l2)) 