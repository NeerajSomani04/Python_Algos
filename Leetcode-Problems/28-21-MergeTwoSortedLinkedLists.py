# In this we are going to solve leetcode #21 problem
# https://leetcode.com/problems/merge-two-sorted-lists/

# we are going to follow a specific process (D, D, P, A, B)
# Definition, Data, Pseudo code, Actual code, Big-O efficiency

## Definition -- Can be easily understood from leetcode problem statement

## Data (IOEA) -- Input, Output, Edge Cases, Assumptions
  # Input -- two linked list L1 and L2
  # Output -- return head of newly merged sorted list 
  # Egde Cases -- list can be empty
  # Assumptions -- 
      Constraints:
        The number of nodes in both lists is in the range [0, 50].
        -100 <= Node.val <= 100
        Both l1 and l2 are sorted in non-decreasing order.


''' Pseudo code  --
      we need to look at each charachter (LOOP)
        - update the charachter count and store it
      look up each charachter in the hash table
        - if its unique (value == 1), return its index value from array
      non are unique, return -1
'''

# Actual code --
# Solution 1:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:
            return l2
        elif l2 == None:
            return l1
        elif l1.val < l2.val:
            head = l1
            l1Cur = l1.next
            l2Cur = l2
        else:
            head = l2
            l2Cur = l2.next
            l1Cur = l1
            
        cur = head
        while l1Cur and l2Cur:
            if l1Cur.val == l2Cur.val:
                cur.next = l1Cur
                l1Cur = l1Cur.next
                cur = cur.next
            elif l1Cur.val < l2Cur.val:
                cur.next = l1Cur
                l1Cur = l1Cur.next
                cur = cur.next
            elif l2Cur.val < l1Cur.val:
                cur.next = l2Cur
                l2Cur = l2Cur.next
                cur = cur.next
        if l1Cur is None:
            cur.next = l2Cur
        elif l2Cur is None:
            cur.next = l1Cur
        return head

'''
Big-O efficiency
time complexity -- O(n) --> in worst case we need to travel all n elements of shortest list
space complexity -- O(1) --> just storing values in few variables
'''

