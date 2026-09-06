# 1002. Find Common Characters
# Easy
# Topics
# premium lock icon
# Companies
# Given a string array words, return an array of all characters that 
# show up in all strings within the words (including duplicates). 
# You may return the answer in any order.

 
# Example 1:
# Input: words = ["bella","label","roller"]
# Output: ["e","l","l"]

# Example 2:
# Input: words = ["cool","lock","cook"]
# Output: ["c","o"]
 
# Constraints:
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] consists of lowercase English letters.


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common = Counter(words[0])

        for word in words[1:]:
            curr = Counter(word)

            for ch in common:
                common[ch] = min(common[ch], curr[ch])

        ans = []

        for ch, count in common.items():
            ans += [ch] * count

        return ans















# Time Complexity
# O(n × m)
# n = number of words
# m = average length of each word
# Space Complexity
# Auxiliary Space: O(1) (26-size frequency arrays)
# Including Output: O(k) (k = number of common characters)