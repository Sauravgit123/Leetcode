# 904. Fruit Into Baskets
# Attempted
# Medium
# Topics
# premium lock icon
# Companies
# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

 

# Example 1:

# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# Example 2:

# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# Example 3:

# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
 

# Constraints:

# 1 <= fruits.length <= 105
# 0 <= fruits[i] < fruits.length


# BRUTE FORCE METHOD
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        m=0
        for i in range(len(fruits)):
            s=set()
            for j in range(i,len(fruits)):
                s.add(fruits[j])
                if len(s)>2:
                    break
                m=max(m,j-i+1)
        return m

# Complexity
# Time: O(n²) 
# Space: O(1) 





#BETTER APPROACH

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        m=0
        l=0
        r=0
        d={}
        while r<len(fruits):
            if fruits[r] not in d:
                d[fruits[r]]=1
                while len(d)>2:
                    d[fruits[l]]-=1
                    if d[fruits[l]]==0:
                        del d[fruits[l]]
                    l+=1
            else:
                d[fruits[r]]+=1
            m=max(m,r-l+1)
            r+=1
        return m

# Complexity
# Time: O(n)
# Space: O(1)           
                
                
# STANDARD APPROACH

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = 0
        d = {}
        ans = 0

        for r in range(len(fruits)):
            d[fruits[r]] = d.get(fruits[r], 0) + 1

            while len(d) > 2:
                d[fruits[l]] -= 1
                if d[fruits[l]] == 0:
                    del d[fruits[l]]
                l += 1

            ans = max(ans, r - l + 1)

        return ans

