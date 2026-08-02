# 155. Min Stack
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Hint
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int value) pushes the element value onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

 

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 

# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.

class MinStack:

    def __init__(self):
        self.items=[]

    def push(self, value: int) -> None:
        if len(self.items)==0:
            self.items.append((value,value))
        else:
            mini=min(self.items[-1][1],value)
            self.items.append((value,mini))
    def pop(self) -> None:
        if self.items:
            self.items.pop()
        else:
            print("Empty Stack")
            return
    def top(self) -> int:
        if self.items:
            return self.items[-1][0]
        else:
            print("Empty Stack")
            return

    def getMin(self) -> int:
        if self.items:
            return self.items[-1][1]
        else:
            print("Empty Stack")
            return
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Time Complexity
# Push      : O(1)
# Pop       : O(1)
# Top       : O(1)
# GetMin    : O(1)

# Space     : O(n)