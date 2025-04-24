""" Easy


DataFrame df1
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

DataFrame df2
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| student_id  | int    |
| name        | object |
| age         | int    |
+-------------+--------+

Write a solution to concatenate these two DataFrames vertically into one DataFrame.

The result format is in the following example. """

import pandas as pd

def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    # Cusamos el metodo concat 
    # los parametros en corchetes son los dos dataframes
    # ignore_index=True para que no se repitan los indices
    result = pd.concat([df1, df2], ignore_index=True)
    
    # Returnamos 
    return result