# 3090. Maximum Length Substring With Two Occurrences
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, return the maximum length of a substring such that it contains at most two occurrences of each character.
 

# Example 1:

# Input: s = "bcbbbcba"

# Output: 4

# Explanation:

# The following substring has a length of 4 and contains at most two occurrences of each character: "bcbbbcba".
# Example 2:

# Input: s = "aaaa"

# Output: 2

# Explanation:

# The following substring has a length of 2 and contains at most two occurrences of each character: "aaaa".
 

# Constraints:

# 2 <= s.length <= 100
# s consists only of lowercase English letters.

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        d={}
        i=0
        j=0
        c=0
        while j<len(s):
            d[s[j]]=d.get(s[j],0)+1
            while d[s[j]]>2:
                d[s[i]]-=1
                if d[s[i]]==0:
                    del d[s[i]]
                i+=1
            c=max(c,j-i+1)
            j+=1
        return c

# Complexity :
# Time: O(n)
# Space: O(1)

        
        