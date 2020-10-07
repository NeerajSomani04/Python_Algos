# In this we are going to solve leetcode #387 problem
# https://leetcode.com/problems/valid-palindrome/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- any printable ASCII characters in the form of string
  # Output -- "true" if valid palindrome, else "false"
  # Egde Cases -- empty string is a valid palindrome, also string might contain special charchter
  # Assumptions -- remove special charachters, also, upper case and lower case letters are same

## Pointer menthod or Pointer Traversal is a great way to solve this problem


''' Pseudo code  --
      we need to look at each charachter (LOOP)
        - update the charachter count and store it
      look up each charachter in the hash table
        - if its unique (value == 1), return its index value from array
      non are unique, return -1
'''
# What is Naive solution:-
   # Its a solution that seems very obvious but usually not very efficient
   # 
    
    
# Actual code --

