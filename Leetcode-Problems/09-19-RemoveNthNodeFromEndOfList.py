# In this we are going to solve leetcode problem #19
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- Given the head of a linked list, remove the nth node from the end of the list 
  # Output -- return head of new linked list
  # Egde Cases -- delete last and first node is tricky
  # Assumptions -- input Linked list can't be empty
        Constraints:
            The number of nodes in the list is sz.
            1 <= sz <= 30
            0 <= Node.val <= 100
            1 <= n <= sz



''' 
Pseudo code  --
      - count length of Linked list
      - calculate index where we need to delete the node
      - tranversing again to delete the node
'''


# Actual code --
## Solution 1:
