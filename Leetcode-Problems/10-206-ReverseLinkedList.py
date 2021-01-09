## Reverse a singly linked list.

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

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
      prev = None
        curr = head
        while curr:    
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
 
## Big-O notation -->
# time complexity --> O(n) --> because of while loop
# space complexity --> O(1) --> only 3 variables used

## Solution 2: this is tail recursion
class Solution:
    def reverseList(self, head: ListNode, prev = None) -> ListNode:   
        if head is None:
            return prev
        temp = head.next
        head.next = prev
        return self.reverseList(temp, head)

## Big-O notation -->
# time complexity --> O(n) --> because of recursive calls, that we do for each node
# space complexity --> O(1) --> although, there is some space that stacks are going to take but garbage collector will through them as we don't need those stack for our calculation. This is because of tail recursive call.


## Solution 3: Normal Recursion
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        node = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return node

## Big-O notation -->
# time complexity --> O(n) --> because of recursive calls, that we do for each node
# space complexity --> O(1) --> although, there is some space that stacks
    

        
