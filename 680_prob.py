# 680. Valid Palindrome II
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

# Example 1:

# Input: s = "aba"
# Output: true
# Example 2:

# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# Example 3:

# Input: s = "abc"
# Output: false
 

# Constraints:

# 1 <= s.length <= 105
# s consists of lowercase English letters.

class Solution:
    def check(self,s):
            i=0
            j=len(s)-1
            while j>i:
                if s[j]==s[i]:
                    j-=1
                    i+=1
                else:
                    return False
            return True
    def validPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        while j>i:
            if s[j]==s[i]:
                j-=1
                i+=1
            else:
                return self.check(s[i+1:j+1]) or self.check(s[i:j])
        return True
         

# Time Complexity: O(N)
# Space Complexity: O(N)       
        
        
        
    
                
        