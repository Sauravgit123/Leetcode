# 520. Detect Capital
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Given a string word, return true if the usage of capitals in it is right.

 

# Example 1:

# Input: word = "USA"
# Output: true
# Example 2:

# Input: word = "FlaG"
# Output: false
 

# Constraints:

# 1 <= word.length <= 100
# word consists of lowercase and uppercase English letters.





# Using in built func (not recommended)

# class Solution:
#     def detectCapitalUse(self, word: str) -> bool:
#         # 1. word.isupper() -> Sab Caps hain (USA)
#         # 2. word.islower() -> Sab Small hain (leetcode)
#         # 3. word.istitle() -> Sirf pehla Cap hai (Google)
#         return word.isupper() or word.islower() or word.istitle()





# use logic
word='USA'                 # USA  ,Usa  usa  all 3 correct
n=len(word)
c=0

for i in word:
    if 'A' <= i <='Z':
        c+=1
if (c==1 and 65 <= ord(word[0]) <=90) or c==n or c==0 :
    print(True)
else:
     print(False)
        

            

            
        
