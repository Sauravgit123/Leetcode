# 22. Generate Parentheses
# Medium
# Topics
# premium lock icon
# Companies
# Given n pairs of parentheses, write a function to generate
#  all combinations of well-formed parentheses.


# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:
# Input: n = 1
# Output: ["()"]
 
# Constraints:
# 1 <= n <= 8


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(s, open, close):
            if len(s) == 2 * n:
                ans.append(s)
                return

            if open < n:
                backtrack(s + "(", open + 1, close)

            if close < open:
                backtrack(s + ")", open, close + 1)

        backtrack("", 0, 0)
        return ans

# Time: O(Cₙ × n) (Catalan number)
# Auxiliary Space: O(n)
# Total Space (including output): O(Cₙ × n)





res=[]
def solve(n,temp,t,c):
    if len(temp)==n:
        res.append(temp)
        return
  
    if c<n//2:
        solve(n,temp+"(",t+1,c+1)
    if t>0:
        solve(n,temp+")",t-1,c)
    return res


n=4

print(solve(2*n,"",0,0))

# Complexity
# Time: O(4^n / √n) (Catalan number of valid combinations)
# Space: O(n) recursion stack (output ko ignore karke)