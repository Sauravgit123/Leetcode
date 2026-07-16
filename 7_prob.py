# 7. Reverse Integer
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

# Example 1:

# Input: x = 123
# Output: 321
# Example 2:

# Input: x = -123
# Output: -321
# Example 3:

# Input: x = 120
# Output: 21
 

# Constraints:

# -231 <= x <= 231 - 1


n=int(input("Enter the number :"))

sign=-1 if n<0 else 1     # ternary operator or inline IF statement

n=abs(n)
rev=0
while n>0:
    dig=n%10
    rev=rev*10+dig
    n=n//10
rev=sign*rev
if rev<-2**31:
    print(0)
elif rev>2**31-1:
    print(0)
else:
    print(rev)





























