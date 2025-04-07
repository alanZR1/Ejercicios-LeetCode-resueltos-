""" Easy

You are given an array of strings names, and an array heights that
consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

  """
  
def sortPeople(names, heights):
    people = list(zip(names, heights))
    people.sort(key = lambda x: x[1], reverse = True)
    sorted_names = []
    for person in people:
        sorted_names.append(person[0])
    return sorted_names
    
names = ["Alice", "Bob", "Bob"]
heights = [155, 185, 150]
print(sortPeople(names, heights))
