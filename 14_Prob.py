# 14. Longest Common Prefix
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.
 





class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mini=min(len(s) for s in strs)
        if not strs:
            return ""

        first_word = strs[0]
        result = ""

        for i in range(len(first_word)):

            ch = first_word[i]

            for word in strs:

                # agar word chhota hai ya mismatch mila → stop
                if i<mini or word[i] == ch:
                    result += ch

                else:
                    return result

        return result
    
    
# Time  : O(n × m)
# Space : O(m)