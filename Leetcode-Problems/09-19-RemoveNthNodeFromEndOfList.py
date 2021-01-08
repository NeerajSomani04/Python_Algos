# In this we are going to solve leetcode problem #19
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement
'''
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

''' 
Pseudo code  --
    - Traverse through list, following ".next"
      - count length of Linked list
      - calculate index where we need to delete the node
      - tranversing again to delete the node, by point around the n node (that we want to delete)
      - handle edge deletion edge case
      - 
'''


# Actual code --
## Solution 1:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # 1. find out length of linked list
        # 2. identify left index of the node that we need to delete (as per question we are given right index of the node)
        # 3. traverse the linkedlist and point around the node
        
        on = head
        length = 1
        while on.next:
            length += 1
            on = on.next
        leftIndex = length - n
        
        on = head
        if leftIndex == 0:
            return on.next
         
        while leftIndex > 1:
            leftIndex -= 1
            on = on.next
        on.next = on.next.next
        return head
      
      
 ## Aaron has calculated the length in a wrong way but conceptually, explaination is good.
# Big-O notation -->
# time complexity --> O(n) --> O(n) + O(n) because of 2 while loop, means 2 traversal
# space complexity --> O(1) --> 

## Solution 2 : Solving the same problem in one traversal:
class Solution:
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for _ in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
      
 
# Big-O notation -->
# time complexity --> O(n) --> O(n) because of 2 while loop, means only one traversal
# space complexity --> O(1) --> 

