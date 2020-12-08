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
        
