# In this we are going to solve leetcode #155 problem
# https://leetcode.com/problems/min-stack/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input --
  # Output --
  # Egde Cases --
  # Assumptions --

# Solution 1:

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minValue = float('inf')

    def push(self, x: int) -> None:
            self.stack.append(x)
            if x < self.minValue:
                self.minValue = x

    def updateMin(self):
        newMin = float('inf')
        for item in self.stack:
            if item < newMin:
                newMin = item
        self.minValue = newMin

    def pop(self) -> None:
        item = self.stack.pop()
        if item == self.minValue:
            self.updateMin()
        return item


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minValue


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
