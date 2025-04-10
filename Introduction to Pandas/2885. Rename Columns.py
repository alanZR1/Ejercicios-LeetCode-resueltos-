""" Easy

+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| id          | int    |
| first       | object |
| last        | object |
| age         | int    |
+-------------+--------+
Write a solution to rename the columns as follows:

id to student_id
first to first_name
last to last_name
age to age_in_years
The result format is in the following example.

  """
  
import pandas as pd

def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    # renombramos las columnas con el metodo rename
    # el parámetro columns recibe un diccionario con los nombres a cambiar
    students.rename(columns = {
        'id': 'student_id',
        'first': 'first_name',
        'last': 'last_name',
        'age': 'age_in_years'
    }, inplace = True)
    # inplace = True modifica el DataFrame original
    
    return students

 