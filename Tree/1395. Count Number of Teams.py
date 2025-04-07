""" Medium

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.

You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]) where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams). """


def numTeams(rating):
    n = len(rating)
    count = 0

    # Para cada soldado en la posición "j", encontrar cuántos soldados antes de él son menores/mayores
    # y cuántos soldados después de él son mayores/menores para formar equipos válidos.
    for j in range(n):
        less_left = less_right = greater_left = greater_right = 0

        # Comparar con los soldados a la izquierda de "j"
        for i in range(j):
            if rating[i] < rating[j]:
                less_left += 1
            elif rating[i] > rating[j]:
                greater_left += 1

        # Comparar con los soldados a la derecha de "j"
        for k in range(j + 1, n):
            if rating[j] < rating[k]:
                less_right += 1
            elif rating[j] > rating[k]:
                greater_right += 1

        # Contar equipos válidos
        count += less_left * less_right + greater_left * greater_right

    return count

rating =   [2,5,3,4,1]
print(numTeams(rating))
