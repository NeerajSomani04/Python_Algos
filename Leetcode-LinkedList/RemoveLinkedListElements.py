'''
question link -- https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/

input --> head and value that needs to be deleted
output --> head
edge case --> 
      1. empty list 
      2. delete head or tail element, or val is not present in list
assumption --> always have one element in list
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
      while head is not None and head.val == val:
            head = head.next
        current = head
        while current is not None:
            if current.next is not None and current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return head

