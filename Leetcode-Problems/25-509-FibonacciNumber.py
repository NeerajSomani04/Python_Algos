# In this we are going to solve leetcode problem #20
# https://leetcode.com/problems/valid-parentheses/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- an interger that represents the position in fibonacci series, that starts with 0
  # Output -- an integer value from fibonacci series for the given position
  # Egde Cases -- if n is zero or 1
  # Assumptions -- Constraints: 0 <= n <= 30

''' 
Pseudo code  --
      - f(n) = f(n - 1) + f (n-2)
      - if n < 2: return 1
      - 
      
'''


# Actual code --
## Solution 1:

class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

'''
## big-O efficiency
# time complexity -- O(n) -- because of n number of run for recursive function
# space complexity -- O(n) -- because of n stack frame

## Leetcode runtime statistics:
Runtime: 964 ms
Memory Usage: 14.3 MB
'''

## Solution 2:-
class Solution:
    def fib(self, N: int) -> int:
        cache = {}
        def recur_fib(N):
            if N in cache:
                return cache[N]

            if N < 2:
                result = N
            else:
                result = recur_fib(N-1) + recur_fib(N-2)

            # put result in cache for later reference.
            cache[N] = result
            return result
        return recur_fib(N)

'''
## big-O efficiency
# time complexity -- O(n) -- because of n number of run for recursive function
# space complexity -- O(k) -- because of k in hash table

## Leetcode runtime statistics:
Runtime: 32 ms
Memory Usage: 14.1 MB
'''

## awesome link for more than 6 different solutions:
https://leetcode.com/explore/learn/card/recursion-i/255/recursion-memoization/1661/discuss/308688/6-Python-solutions


