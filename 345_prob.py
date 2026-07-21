# 345. Reverse Vowels of a String
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear 
# in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"

 

# Constraints:

# 1 <= s.length <= 3 * 105
# s consist of printable ASCII characters.



class Solution:
    def reverseVowels(self, s: str) -> str:
        v=[]
        for i in s:
            if i=='a' or i=='e' or i=='i' or i=='o' or i=='u'or i=='A' or i=='E' or i=='I'or i=='O' or i=='U':
                v.append(i)
        v=v[::-1]
        s1=[]
        for i in s:
            s1.append(i)
        i=0
        j=0
        while i<len(s1):
            if s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u' or s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
                s1[i]=v[j]
                j+=1
            i+=1
        ans=""
        for i in range(len(s1)):
            ans+=s1[i]
        return ans

# Complexity:
# Time: O(n)
# Space: O(n) (vowels list + string list)



class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and s[left] not in vowels:
                left += 1

            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)
    
# Time: O(n)
# Space: O(1)