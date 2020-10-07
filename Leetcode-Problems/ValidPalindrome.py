# In this we are going to solve leetcode #387 problem
# https://leetcode.com/problems/first-unique-character-in-a-string/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- any string charachter is allowed
  # Output -- single interger (that represent index value of first unique charachter and "-1" if no unique charachter)
  # Egde Cases -- An array can be empty or An array can have no unique charachter
  # Assumptions -- An array can contain only alphabets in lowercase, and no numerical or special charachter

''' Pseudo code  --
      we need to look at each charachter (LOOP)
        - update the charachter count and store it
      look up each charachter in the hash table
        - if its unique (value == 1), return its index value from array
      non are unique, return -1
'''

# Actual code --
