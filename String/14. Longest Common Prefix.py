""" Write a function to find the longest common prefix
string amongst an array of strings.

If there is no common prefix, return an empty string "". """

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        # Start with the first string as the prefix
        sorted_str = sorted(strs)
        prefix = ""
        first = sorted_str[0]
        last = sorted_str[-1]
        
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return prefix
            prefix += first[i]
        return prefix
        
        

result = Solution()
strs = ["dog","dogear","car"]
print(result.longestCommonPrefix(strs))  # Output: "fl"