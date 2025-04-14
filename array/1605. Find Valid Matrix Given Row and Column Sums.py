""" Medium
Topics
Companies
Hint
You are given two arrays rowSum and colSum of non-negative integers where rowSum[i]
is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words,
you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. 
It's guaranteed that at least one matrix that fulfills the requirements exists.

  """
  
def restoreMatrix(rowSum, colSum):
    # medimos la longitud de las filas y columnas
    m, n = len(rowSum), len(colSum)
    # creamos una matriz de ceros
    matriz = [[0] * n for j in range(m)]
    # recorremos la matriz
    for i in range(m):
        for j in range(n):
            # tomamos el valor mínimo entre la suma de la fila y la columna	
            val = min(rowSum[i], colSum[j])
            # asignamos el valor a la matriz
            matriz[i][j] = val
            # restamos el valor a la suma de la fila y la columna
            rowSum[i] -= val
            colSum[j] -= val
    return matriz


rowSum = [3,8]
colSum = [4,7]
print(restoreMatrix(rowSum, colSum))