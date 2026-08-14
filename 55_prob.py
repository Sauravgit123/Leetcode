# 55. Jump Game
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

 

# Example 1:

# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:

# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
 

# Constraints:

# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        m=0

        for i in range(0,len(nums)):
            if i>m:
                return False
            m=max(m,i+nums[i])
        return True

# m = farthest index reachable so far.
# If current index > m, we can't reach it -> False.
# Continuously update the farthest reachable index.

# Time Complexity - O(n)
# Space Complexity - O(1)





class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # Dictionary to store already computed answers.
        # Key = current index
        # Value = True/False (can we reach the last index from here?)
        dp = {}

        def solve(i):

            # Base Case:
            # If we have reached or crossed the last index,
            # then the answer is True.
            if i >= len(nums) - 1:
                return True

            # If this index has already been solved,
            # return the stored answer instead of solving again.
            if i in dp:
                return dp[i]

            # Try every possible jump from the current index.
            # Example:
            # nums[i] = 3
            # We can jump 1, 2, or 3 steps.
            for jump in range(1, nums[i] + 1):

                # If any jump reaches the end,
                # store True for this index and return.
                if solve(i + jump):
                    dp[i] = True
                    return True

            # None of the jumps worked.
            # Store False so we don't calculate this index again.
            dp[i] = False
            return False

        # Start recursion from index 0.
        return solve(0)


# Time Complexity: O(n²)
# Space Complexity: O(n)



# solve(0)
# │
# ├── jump = 1 → solve(1)   ← Recursion ALWAYS tries first jump first
# │      │
# │      ├── jump = 1 → solve(2)
# │      │      │
# │      │      └── jump = 1 → solve(3)
# │      │             │
# │      │             └── jump = 1 → solve(4) ✅ True
# │      │
# │      ├── jump = 2 → (Not tried, already got True)
# │      └── jump = 3 → (Not tried)
# │
# └── jump = 2 → (Not tried)



# solve(i) = Can I reach the end from index i?

# Example:
# 0 -> (1,2)
# 1 -> (1,2,3)

# Recursion first tries:
# 0→1→2→3→4

# If True is found, it stops.
# Otherwise it backtracks and tries the next jump.