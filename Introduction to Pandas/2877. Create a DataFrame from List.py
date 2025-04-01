""" 2877. Create a DataFrame from List
Solved
Easy
Companies
Hint
Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.

The result format is in the following example.
Example 1:

Input:
student_data:
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+
Explanation:
A DataFrame was created on top of student_data, with two columns named student_id and age.
  """

import pandas as pd



def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    # creamos una dataframe de una lista de listas
    # el parametro colums indica que nombre de le pondran a las columnas 
    # en esta caso cada lista tiene dos elementos, el primero es el id del estudiante y el segundo su edad
    # el resultado es un dataframe con dos columnas, student_id y age
    
    df = pd.DataFrame(student_data, columns=['student_id', 'age'])
    
    return df

# Ejemplo

#dataFrame Ejemplo
student_data = [[1,15],[2,11],[3,11],[4,20]]
df = createDataframe(student_data)
print(df)