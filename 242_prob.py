# 242. Valid Anagram
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

 

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

 

# Constraints:

# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.
 

# Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?



# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         return sorted(s) == sorted(t)
    
# Time: O(n log n) 
# Space: O(n)




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq = {}

        # count characters in s
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # subtract using t
        for ch in t:
            if ch not in freq:
                return False

            freq[ch] -= 1

            if freq[ch] == 0:
                del freq[ch]

        return len(freq) == 0
    
# Time: O(n) 
# Space: O(1)