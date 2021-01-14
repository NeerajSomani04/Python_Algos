## Reverse a singly linked list.

# In this we are going to solve leetcode problem #700
# https://leetcode.com/problems/search-in-a-binary-search-tree/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- given a root node of a BST (meaning its balanced)
  # Output -- root node of sub-BST
  # Egde Cases -- 
  # Assumptions -- If such a node does not exist, return null


''' 
Pseudo code  --
      - while there is a list
        - save .next in temp variable
        - set .next to prev
        - set prev to current node
        - advance current node
'''


# Actual code --
## Solution 1:
