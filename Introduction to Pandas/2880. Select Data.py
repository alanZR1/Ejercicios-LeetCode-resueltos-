""" 2880. Select Data

DataFrame students
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to select the name and age of the student with student_id = 101.

The result format is in the following example.

 

Example 1:
Input:
+------------+---------+-----+
| student_id | name    | age |
+------------+---------+-----+
| 101        | Ulysses | 13  |
| 53         | William | 10  |
| 128        | Henry   | 6   |
| 3          | Henry   | 11  |
+------------+---------+-----+
Output:
+---------+-----+
| name    | age | 
+---------+-----+
| Ulysses | 13  |
+---------+-----+
Explanation:
Student Ulysses has st """

import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    
    return students.loc[students['student_id'] == 101, ['name', 'age']]

    """El método loc obtiene el usuario con el primer parámetro dado,
        el segundo parametro indica la selección de columnas a mostrar, 
        por default muestra toda la info
    """