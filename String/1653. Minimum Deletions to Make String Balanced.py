""" Medium

You are given a string s consisting only of characters 'a' and 'b'​​​​.

You can delete any number of characters in s to make s balanced.
s is balanced if there is no pair of indices (i,j) such that i < j and s[i] = 'b' and s[j]= 'a'.

Return the minimum number of deletions needed to make s balanced.

  """



def minimumDeletions(s):
    count_b = 0
    deletions = 0

    for char in s:
        if char == 'b':
            count_b += 1
        else:
            deletions = min(deletions + 1, count_b) 
    return deletions

s = "aababbab"
print(minimumDeletions(s))