## 23 --  https://leetcode.com/problems/merge-k-sorted-lists/

''' All below approach has this Big-O efficiency
Time complexity #
Since we’ll be going through all the elements of all arrays and will be removing/adding one element to the heap in each step, the time complexity of the above algorithm will be O(N*logK),O(N∗logK), where ‘N’ is the total number of elements in all the ‘K’ input arrays.

Space complexity #
The space complexity will be O(K)O(K) because, at any time, our min-heap will be storing one number from all the ‘K’ input arrays.
'''

# Solution 1: Using Queue (this will work with python (not python3) on leetcode
from Queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next

## Solution 3: This works with python3

import queue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        sorted_list_head = sorted_list_tail = ListNode(0)
        
        pq = queue.PriorityQueue()
        
        def add_node_in_pq(idx, node):
            if node:
                pq.put((node.val, idx, node))
        
        for idx, node in enumerate(lists):
            add_node_in_pq(idx, node)
        
        while not pq.empty():
            _, idx, node = pq.get()
            add_node_in_pq(idx, node.next)
            node.next = None
            sorted_list_tail.next = node
            sorted_list_tail = sorted_list_tail.next
        
        return sorted_list_head.next

## Solution 4: using divide and conquer

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        mid = len(lists) // 2
        l, r = self.mergeKLists(lists[:mid]), self.mergeKLists(lists[mid:])
        return self.merge(l, r)
    
    def merge(self, l, r):
        dummy = p = ListNode()
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next
      
    '''
    def merge1(self, l, r):
        if not l or not r:
            return l or r
        if l.val< r.val:
            l.next = self.merge(l.next, r)
            return l
        r.next = self.merge(l, r.next)
        return r
    '''
