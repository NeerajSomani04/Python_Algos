# In this we are going to solve leetcode problem #20
# https://leetcode.com/problems/valid-parentheses/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- string containing just these characters '(', ')', '{', '}', '[' and ']', 
  # Output -- "true" if the input string is valid, else "false"
  # Egde Cases -- empty string is a valid string, string can have only one paranthesis like '[' or '}'
  # Assumptions -- string will contain only paranthesis charachters mentioned above

'''
In this we are going to use Stack. 
  - A very important thing to understand in each problem, which data structure and method (process) will give you optimum result.
  - This can only be possible if you understand the behaviour of each data structure.
  - A stack is an array with more specific rules, Last in First Out
'''

''' 
Pseudo code  --
      - Break a big string input to smaller chunks, known as chunking
      - for char in string
        - if opening, push into stack
        - if closing, pop and compare
          - if test fails, return false
        - if all passed, return true
'''


# Actual code --
## Solution 1:
class Solution:
  def isValid(self, s: str) -> bool:
    p_dict = { '(' : ')' , '{' : '}' ,   '[' : ']' }
    stack = []
    for _ in s :
        if _ in p_dict.keys() :
          stack.append(_)
        else:
          if len(stack) == 0 :
            return False
          if p_dict[stack.pop()] != _ :
            return False
    if len(stack) > 0 :
        return False
    else:
        return True 
      

''' 
Big-O Efficiency -->

# time complexity --> O(n) because of for loop
# space complexity --> O(n) because stack array needs to hold all paranthesis, if needed


