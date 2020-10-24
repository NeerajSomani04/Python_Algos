Reverse a singly linked list.

# In this we are going to solve leetcode problem #206
# https://leetcode.com/problems/reverse-linked-list/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- given a head node of a singly linked list
  # Output -- head node of reversed linked list
  # Egde Cases -- only head node in linked list
  # Assumptions -- linked list can't be empty


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
