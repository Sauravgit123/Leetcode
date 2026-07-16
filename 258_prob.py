# 258. Add Digits
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

# Example 1:

# Input: num = 38
# Output: 2
# Explanation: The process is
# 38 --> 3 + 8 --> 11
# 11 --> 1 + 1 --> 2 
# Since 2 has only one digit, return it.
# Example 2:

# Input: num = 0
# Output: 0
 

# Constraints:

# 0 <= num <= 231 - 1


# USING WHILE LOOP

# n=(int(input("Enter the number : ")))

# while n>9:
#     s=0
#     while n:
#         s+=n%10
#         n=n//10
#     n=s
# print(n)
    


# USING RECURSION

def summ(n):
    s=0
    if n<10:
        return n
    # sum() adds up the list comprehension directly
    s = sum(int(i) for i in str(n))
    return summ(s)


n=(int(input("Enter the number : ")))
print(summ(n))





























































