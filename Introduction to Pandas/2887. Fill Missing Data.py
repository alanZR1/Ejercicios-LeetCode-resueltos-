""" Easy


DataFrame products
+-------------+--------+
| Column Name | Type   |
+-------------+--------+
| name        | object |
| quantity    | int    |
| price       | int    |
+-------------+--------+
Write a solution to fill in the missing value as 0 in the quantity column.

The result format is in the following example. """

import pandas as pd

def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    # ocupamos el metodo fillna para llenar los valores nulos de la columna quantity con 0
    # seleccionando la columna quantity y aplicando el metodo fillna
    # y asigando el resultado a la misma columna quantity
    products['quantity'] = products['quantity'].fillna(0)
    return products