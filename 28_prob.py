# 28. Find the Index of the First Occurrence in a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:


        if needle in haystack:
            r=haystack.index((needle))
            return r
        else:
            return -1


# Time Complexity = O(n × m)
# Reason: needle in haystack searches the substring, and haystack.index(needle) searches again. In the worst case, each search takes O(n × m).

# Space Complexity = O(1)
# Reason: No extra data structure is used; only a variable (r) is stored.