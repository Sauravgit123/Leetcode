# 1189. Maximum Number of Balloons
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string text, you want to use the characters of text to 
# form as many instances of the word "balloon" as possible.

# You can use each character in text at most once. Return 
# the maximum number of instances that can be formed.

 

# Example 1:



# Input: text = "nlaebolko"
# Output: 1
# Example 2:



# Input: text = "loonbalxballpoon"
# Output: 2
# Example 3:

# Input: text = "leetcode"
# Output: 0
 

# Constraints:

# 1 <= text.length <= 104
# text consists of lower case English letters only.
 

# Note: This question is the same as 2287: Rearrange Characters to Make Target String.

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        b = {"b": 0,"a": 0,"l": 0,"o": 0,"n": 0}
        i=0
        while i<len(text):
            if text[i] in b:
                b[text[i]]+=1
            i+=1
        b["l"]//=2
        b["o"]//=2
        return min(b.values())

# Time Complexity = O(n)
# Space Complexity =O(1)