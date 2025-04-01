
def isArraySpecial( nums, queries):
    n = len(nums)
    com = [0]*n
    ans = []
    for i in range(1, n):
        com[i] = com[i - 1]
        if nums[i] % 2 == nums[i - 1] % 2:
            com[i] += 1
    for q in queries:
        x, y = q
        falseCount = com[y] - (com[x] if x > 0 else 0)
        if falseCount and x != y:
            ans.append(False)
        else:
            ans.append(True)
    return ans
        
nums = [3, 4, 1, 2, 6]
queries = [[0, 4], [1, 3], [3, 3]]

print(isArraySpecial(nums, queries))
