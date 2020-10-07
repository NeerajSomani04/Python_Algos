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
# Solution 1:

def first_unique_char(s):
  hash_table = {}
  for char in s:
    if char in hash_table:
      hash_table[char] += 1
    else:
      hash_table[char] = 1
  
  for i, char in enumerate(s):
    if hash_table[char] == 1:
      return i
  
  return -1

## Big-O efficiency --
# Time complexity : O(n) + O(n) ==> O(2n) ==> O(n) ----> this is linear time
# space complexity: O(26) ==> O(1)
    # this is tricky, you might be thinking hash table will store n char of array into hash table, but in reality its not true, at max you can have only 26 char in hash table.

    ## question for Aaron:- why he is referring 32 charachter, while calculating space complexity.
    
# Solution 2:
def first_unique_char(s):
  for i, char in s:
    if s.index(char) == s.rindex(char):
      return i
  
  return -1

## Big-O efficiency -- 
# Time complexity : O(n) * (O(n) + O(n)) ==> O(n) * O(2n) ==> O(n ^ 2) ----> this is quadratic time
    # each index operation inside a for loop is of O(n) time complexity and for loop itself is O(n) time complexity
# space complexity: O(1) 
    # as we are not using any data structure to store data.
        

## Summary -- Solution 2 is less efficient than Solution 1.





