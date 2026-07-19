# 316. Remove Duplicate Letters
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s, remove duplicate letters so that every letter appears
#  once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

 

# Example 1:

# Input: s = "bcabc"
# Output: "abc"
# Example 2:

# Input: s = "cbacdcbc"
# Output: "acdb"
 

# Constraints:

# 1 <= s.length <= 104
# s consists of lowercase English letters.
 

# Note: This question is the same as 1081: https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        vis = [0] * 26
        num = [0] * 26

        for ch in s:
            num[ord(ch) - ord("a")] += 1

        stk = []

        for ch in s:
            idx = ord(ch) - ord("a")

            if not vis[idx]:
                while stk and stk[-1] > ch:
                    top_idx = ord(stk[-1]) - ord("a")

                    if num[top_idx] > 0:
                        vis[top_idx] = 0
                        stk.pop()
                    else:
                        break

                vis[idx] = 1
                stk.append(ch)

            num[idx] -= 1

        return "".join(stk)

# Time  : O(n)
# Space : O(1)