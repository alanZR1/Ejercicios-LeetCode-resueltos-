""" Easy

You are given an array of strings names, and an array heights that
consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

  """
  
def sortPeople(names, heights):
    # convertir las listas en una lista de tuplas (nombre, altura)
    people = list(zip(names, heights))
    # ordenar la lista de tuplas por altura en orden descendente
    # el segundo elemento de la tupla es la altura
    people.sort(key = lambda x: x[1], reverse = True)
    # crear una lista de nombres ordenados
    sorted_names = []
    for person in people:
        # agregar el nombre a la lista de nombres ordenados
        # el primer elemento de la tupla es el nombre
        sorted_names.append(person[0])
    return sorted_names
    
names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]
print(sortPeople(names, heights))
# Output: ['Bob', 'Alice', 'Bob']
