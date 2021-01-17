# In this we are going to solve leetcode #50 problem
# https://leetcode.com/problems/powx-n/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- x and n is given, where, calculates x raised to the power n (i.e. xn).
  # Output -- float value that represent the calculation result
  # Egde Cases -- 
  # Assumptions -- 
        Constraints:
          -100.0 < x < 100.0
          -231 <= n <= 231-1
          -104 <= xn <= 104

''' Pseudo code  --
      we need to look at each charachter (LOOP)
        - update the charachter count and store it
      look up each charachter in the hash table
        - if its unique (value == 1), return its index value from array
      non are unique, return -1
'''

# Actual code --
# Solution 1:
class Solution:
    def myPow(self, x, n):
        if not n:
            return 1
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n % 2: # this condition is to handle odd power numbers
            return x * self.myPow(x, n-1)
        return self.myPow(x*x, n/2) # this condition is to handle even power numbers

'''
Big-O efficiency --
Time complexity : O(n) ----> becasue there will be n recursive call in worst case of odd power number
Space complexity: O(n) --> because of n recursive stack frame
# leetcode statistics
Runtime: 28 ms
Memory Usage: 14.4 MB
'''

## Solution explained in a very nice way --
## https://leetcode.com/explore/learn/card/recursion-i/256/complexity-analysis/2380/discuss/738830/Python-recursive-O(log-n)-solution-explained


# Solution 2:
class Solution:
    def myPow(self, x, n):
        if abs(x) < 1e-40: return 0 
        if n == 0: return 1
        if n < 0: return self.myPow(1/x, -n)
        lower = self.myPow(x, n//2)
        if n % 2 == 0: return lower*lower
        if n % 2 == 1: return lower*lower*x

'''
Big-O efficiency --
Time complexity : O(log n) ----> becasue we did calculation by dividing the power
Space complexity: O(log n) --> because of "log n" recursive call stack frame
# leetcode statistics
Runtime: 32 ms
Memory Usage: 14.3 MB
'''

# Solution 3: iterative solution
class Solution:
    def myPow(self, x, n):
        if n < 0:
            x = 1 / x
            n = -n
        pow = 1
        while n:
            if n & 1:
                pow *= x
            x *= x
            n >>= 1 
        return pow

'''
## Notes
if n & 1 was same as: if n % 2
n >> 1 was same as : n //= 2
'''

'''
Big-O efficiency --
Time complexity : O(n) ----> becasue there will be n recursive call in worst case of odd power number
Space complexity: O(1) --> because of n recursive stack frame
# leetcode statistics
Runtime: 28 ms
Memory Usage: 14.4 MB
'''

# Solution 4: iterative solution
## We can create this solution with time complexity of O(log n) and space complexity of O(1) by using above 2 approach. It would be iterative solution.

