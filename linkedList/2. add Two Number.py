""" Medium


You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero,
except the number 0 itself.
 """
 
# en leetCode una linked-list se defina como una clase, 
# por lo que se debe importar la clase ListNode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val # valor del nodo
        self.next = next # donde next es un puntero a otro nodo de la lista
        
        
def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    node = ListNode()  # Nodo dummy para simplificar la construcción de la lista resultante
    actual = node
    acarreo = 0  # Acarreo inicial
    
    while l1 or l2 or acarreo:
        # Obtener valores de los nodos actuales (o 0 si ya no hay nodos)
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        
        # Calcular suma y acarreo
        total = val1 + val2 + acarreo
        # El nuevo acarreo es la parte entera de la división entre 10
        acarreo = total // 10
        # El dígito actual es el residuo de la división entre 10
        # Esto asegura que el dígito esté entre 0 y 9
        digit = total % 10
        
        # Crear nuevo nodo y avanzar
        # Se asigna el valor del dígito al nodo actual
        actual.next = ListNode(digit)
        # Avanzar al siguiente nodo de la lista resultante
        actual = actual.next
        
        # Mover l1 y l2 si existen
        if l1:
            # Avanzar al siguiente nodo de l1
            l1 = l1.next
        if l2:
            # Avanzar al siguiente nodo de l2
            l2 = l2.next
    
    return node.next  # El primer nodo real es node.next